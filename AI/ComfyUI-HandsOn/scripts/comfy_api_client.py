#!/usr/bin/env python3
"""Submit an API-format ComfyUI workflow and optionally download its outputs.

Only the Python standard library is used, so the script can run from Windows or
Jetson without installing requests.  Export a workflow with ComfyUI's
"Save (API Format)" menu before using this script.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any


def request_json(url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {error.code} from {url}: {body}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Cannot connect to {url}: {error.reason}") from error


def set_input(
    workflow: dict[str, Any], node_id: str, input_name: str, value: Any
) -> None:
    try:
        node = workflow[node_id]
        inputs = node["inputs"]
    except (KeyError, TypeError) as error:
        raise ValueError(
            f"Node {node_id!r} or its inputs are missing. "
            "Check the API-format JSON and the node ID."
        ) from error

    if input_name not in inputs:
        available = ", ".join(sorted(inputs))
        raise ValueError(
            f"Input {input_name!r} is not on node {node_id}. Available: {available}"
        )
    inputs[input_name] = value


def submit(server: str, workflow: dict[str, Any], client_id: str) -> str:
    result = request_json(
        f"{server}/prompt", {"prompt": workflow, "client_id": client_id}
    )
    if "prompt_id" not in result:
        raise RuntimeError(f"ComfyUI did not return prompt_id: {result}")
    return str(result["prompt_id"])


def wait_for_history(
    server: str, prompt_id: str, timeout: int, poll_interval: float
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        history = request_json(f"{server}/history/{prompt_id}")
        if prompt_id in history:
            return history[prompt_id]
        time.sleep(poll_interval)
    raise TimeoutError(f"Timed out after {timeout}s waiting for {prompt_id}")


def safe_filename(name: str) -> str:
    return Path(name).name.replace("\x00", "_")


def download_outputs(
    server: str, prompt_id: str, history_item: dict[str, Any], output_dir: Path
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded: list[Path] = []

    for node_output in history_item.get("outputs", {}).values():
        for image in node_output.get("images", []):
            filename = str(image["filename"])
            query = urllib.parse.urlencode(
                {
                    "filename": filename,
                    "subfolder": image.get("subfolder", ""),
                    "type": image.get("type", "output"),
                }
            )
            target = output_dir / f"{prompt_id[:8]}_{safe_filename(filename)}"
            try:
                with urllib.request.urlopen(f"{server}/view?{query}", timeout=60) as response:
                    target.write_bytes(response.read())
            except (urllib.error.HTTPError, urllib.error.URLError) as error:
                raise RuntimeError(f"Failed to download {filename}: {error}") from error
            downloaded.append(target)
    return downloaded


def load_jobs(args: argparse.Namespace) -> list[tuple[str | None, int | None]]:
    if args.csv:
        jobs: list[tuple[str | None, int | None]] = []
        with args.csv.open("r", encoding="utf-8-sig", newline="") as file:
            for row_number, row in enumerate(csv.DictReader(file), start=2):
                prompt = (row.get("prompt") or "").strip()
                seed_text = (row.get("seed") or "").strip()
                if not prompt:
                    raise ValueError(f"CSV row {row_number}: prompt is empty")
                seed = int(seed_text) if seed_text else None
                jobs.append((prompt, seed))
        if not jobs:
            raise ValueError("CSV contains no jobs")
        return jobs

    if args.prompt is None and args.seed is None:
        return [(None, None)]
    return [(args.prompt, args.seed)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Submit a ComfyUI API-format workflow."
    )
    parser.add_argument("--workflow", required=True, type=Path)
    parser.add_argument("--server", default="http://127.0.0.1:8188")
    parser.add_argument("--prompt-node", help="Positive CLIP Text Encode node ID")
    parser.add_argument("--prompt-input", default="text")
    parser.add_argument("--seed-node", help="KSampler node ID")
    parser.add_argument("--seed-input", default="seed")
    parser.add_argument("--prompt")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--csv", type=Path, help="CSV with prompt,seed columns")
    parser.add_argument("--wait", action="store_true")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--poll-interval", type=float, default=1.0)
    parser.add_argument("--download-dir", type=Path)
    args = parser.parse_args()

    if args.csv and (args.prompt is not None or args.seed is not None):
        parser.error("Use either --csv or --prompt/--seed, not both")
    if (args.prompt is not None or args.csv) and not args.prompt_node:
        parser.error("--prompt-node is required when changing a prompt")
    if (args.seed is not None or args.csv) and not args.seed_node:
        parser.error("--seed-node is required when changing a seed")
    if args.download_dir and not args.wait:
        parser.error("--download-dir requires --wait")
    return args


def main() -> int:
    args = parse_args()
    server = args.server.rstrip("/")
    base_workflow = json.loads(args.workflow.read_text(encoding="utf-8"))
    jobs = load_jobs(args)
    client_id = str(uuid.uuid4())

    for index, (prompt, seed) in enumerate(jobs, start=1):
        workflow = copy.deepcopy(base_workflow)
        if prompt is not None:
            set_input(workflow, args.prompt_node, args.prompt_input, prompt)
        if seed is not None:
            set_input(workflow, args.seed_node, args.seed_input, seed)

        prompt_id = submit(server, workflow, client_id)
        print(f"[{index}/{len(jobs)}] submitted prompt_id={prompt_id}")

        if args.wait:
            history_item = wait_for_history(
                server, prompt_id, args.timeout, args.poll_interval
            )
            status = history_item.get("status", {})
            if status.get("status_str") == "error":
                raise RuntimeError(f"ComfyUI execution failed: {status}")
            print(f"[{index}/{len(jobs)}] completed prompt_id={prompt_id}")
            if args.download_dir:
                files = download_outputs(
                    server, prompt_id, history_item, args.download_dir
                )
                for file in files:
                    print(f"downloaded {file}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, TimeoutError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
