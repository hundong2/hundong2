# API 실습 스크립트 사용법

## 1. workflow 준비

ComfyUI에서 정상 실행되는 workflow를 만든 뒤 `Save (API Format)`으로 `workflow_api.json`을 저장한다. 일반 UI workflow JSON과 API JSON은 용도가 다르다.

API JSON에서 다음을 찾는다.

```json
"6": {
  "inputs": {
    "text": "기존 positive prompt"
  },
  "class_type": "CLIPTextEncode"
}
```

이 예에서 prompt node ID는 `6`, input 이름은 `text`다. KSampler의 `class_type`을 찾아 seed node ID도 확인한다.

처음부터 만들기 어렵다면 [최소 API workflow 예제](../examples/workflow_api_minimal.example.json)의 `REPLACE_WITH_YOUR_SD15_MODEL.safetensors`를 실제 `models/checkpoints`의 파일명으로 바꾼다. 이 파일은 API 제출용이라 UI 편집 화면용 JSON을 대신하지 않는다.

## 2. 연결 확인만 하기

workflow를 수정하지 않고 그대로 제출한다.

```powershell
python .\comfy_api_client.py --workflow .\workflow_api.json
```

## 3. prompt와 seed 변경

```powershell
python .\comfy_api_client.py `
  --workflow .\workflow_api.json `
  --prompt-node 6 --seed-node 3 `
  --prompt "a friendly robot, clean illustration" `
  --seed 42 `
  --wait `
  --download-dir .\downloaded
```

Linux/Jetson에서는 줄 연결 문자를 백틱 대신 `\`로 쓴다.

```bash
python3 ./comfy_api_client.py \
  --server http://127.0.0.1:8188 \
  --workflow ./workflow_api.json \
  --prompt-node 6 --seed-node 3 \
  --prompt "a friendly robot, clean illustration" \
  --seed 42 --wait --download-dir ./downloaded
```

## 4. CSV 배치 실행

```powershell
python .\comfy_api_client.py `
  --workflow .\workflow_api.json `
  --prompt-node 6 --seed-node 3 `
  --csv ..\examples\prompts.csv `
  --wait --download-dir .\downloaded
```

이 스크립트는 Jetson 과부하를 피하기 위해 CSV 작업을 순차 처리한다.

## 5. 주의사항

- 신뢰할 수 없는 workflow는 unknown custom node를 요구할 수 있다.
- node ID는 workflow를 편집/재저장하면 바뀔 수 있다.
- ComfyUI의 로컬 API에는 기본 인증이 없다. 외부 인터넷에 공개하지 않는다.
- workflow의 Save Image 노드가 실행되어야 내려받을 이미지가 history에 나타난다.
- 운영 환경에서는 인증, 요청 크기 제한, queue 제한, 로깅을 갖춘 별도 API를 앞에 둔다.
