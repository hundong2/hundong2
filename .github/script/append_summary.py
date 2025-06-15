import os
import subprocess
import requests

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
PROMPT = "다음 문서를 한국어로 요약해줘:"

def get_changed_files():
    result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1'], stdout=subprocess.PIPE)
    files = result.stdout.decode().splitlines()
    return [f for f in files if f.endswith('.md') or f.endswith('.txt')]

def summarize_with_gemini(text):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [
            {
                "parts": [
                    {"text": f"{PROMPT}\n{text}"}
                ]
            }
        ]
    }
    resp = requests.post(url, headers=headers, json=body)
    resp.raise_for_status()
    return resp.json()["candidates"][0]["content"]["parts"][0]["text"]

def append_summary_to_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    summary = summarize_with_gemini(content)
    with open(path, 'a', encoding='utf-8') as f:
        f.write("\n\n---\n### Gemini 요약\n")
        f.write(summary.strip())

if __name__ == "__main__":
    changed_files = get_changed_files()
    for file in changed_files:
        append_summary_to_file(file)