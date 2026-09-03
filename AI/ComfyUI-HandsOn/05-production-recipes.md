# 05. 실무 중심 레시피

## 1. 실무 workflow의 기본 원칙

- 입력, 처리, 출력 영역을 시각적으로 그룹화하고 노드에 메모를 남긴다.
- 모델·LoRA·custom node 버전과 라이선스를 기록한다.
- 랜덤 탐색용 workflow와 재생산용 workflow를 분리한다.
- 승인된 seed와 설정은 고정하고 API JSON을 버전 관리한다.
- 사람의 최종 검수 단계를 제거하지 않는다.

## 레시피 A. 제품 배경 시안 만들기

### 용도

촬영 전 콘셉트 검토, 배너 배경 후보 생성. 실제 상품의 형태·라벨을 생성형 모델에 맡기는 용도가 아니다.

### 흐름

```text
상품 누끼 PNG + 마스크
    → 배경 영역만 inpainting/outpainting
    → 색/조명 후보 4종 생성
    → 사람이 상품 왜곡·텍스트·상표 검수
    → 편집 도구에서 최종 합성
```

### 실습

1. 사용 권한이 있는 상품 PNG를 준비한다.
2. 상품 자체는 보호하고 배경만 흰 마스크로 선택한다.
3. prompt 예: `minimal studio background, warm beige gradient, soft shadow, commercial product photography`
4. seed를 고정하고 배경 색 표현만 세 가지로 바꾼다.
5. 결과표에 원본 보존 여부, 그림자 방향, 색상 일관성을 기록한다.

## 레시피 B. 캐릭터/브랜드 시안 일관성 실험

### 용도

아이디어 탐색용 스타일 보드. 상표 등록, 캐릭터 권리 검토는 별도다.

### 흐름

- 승인된 checkpoint + 라이선스 확인된 LoRA
- 고정 seed 묶음
- 표준 prompt template
- 정면/측면/행동별 ControlNet 또는 reference 조건
- 동일한 후처리/업스케일

### prompt template

```text
[subject], [pose], [camera], [environment], [lighting], [style], [quality constraints]
```

예:

```text
a friendly orange delivery robot, front view, eye-level camera,
clean white studio, softbox lighting, flat concept art, simple readable silhouette
```

한 번에 여러 요소를 바꾸지 말고 pose → camera → lighting 순으로 실험한다.

## 레시피 C. 마케팅 소재 배치 생성

### 목표

CSV의 프롬프트를 API로 순서대로 제출한다.

### 준비

1. 완성된 workflow를 `Save (API Format)`으로 내보낸다.
2. API JSON을 열어 positive prompt 노드 ID와 KSampler seed 노드 ID를 찾는다.
3. [examples/prompts.csv](examples/prompts.csv)를 수정한다.
4. [scripts/comfy_api_client.py](scripts/comfy_api_client.py)를 실행한다.

PowerShell 예:

```powershell
python .\scripts\comfy_api_client.py `
  --workflow .\lab01_txt2img_api.json `
  --prompt-node 6 `
  --seed-node 3 `
  --prompt "a clean product background, blue gradient" `
  --seed 101
```

Jetson을 호출할 때:

```powershell
python .\scripts\comfy_api_client.py `
  --server http://JETSON_IP:8188 `
  --workflow .\lab01_txt2img_api.json `
  --prompt-node 6 --seed-node 3 `
  --prompt "a clean product background, blue gradient" `
  --seed 101 --wait --download-dir .\api-output
```

노드 ID는 workflow마다 다르다. 예제의 `6`, `3`을 무조건 복사하지 않는다.

### 운영 시 추가할 것

- 요청 ID와 prompt/seed/model을 로그로 남김
- 최대 queue 크기와 동시 실행 제한
- 실패 재시도 횟수와 timeout
- 산출물 검수 상태와 승인자
- 입력/출력 보존 기간

## 레시피 D. 현장 장비용 Jetson 이미지 생성 서비스

### 권장 구조

```text
사용자 앱 → 사내 API(인증·검증·queue 제한) → Jetson ComfyUI(내부 LAN)
                                      ↓
                              승인된 workflow/모델만 사용
```

ComfyUI 8188을 인터넷에 직접 공개하지 않는다. 상위 API에서 prompt 길이, 해상도, batch, 허용 workflow를 제한한다. Jetson에서는 고정된 경량 workflow와 모델만 배포하고 설계 기능은 Windows 개발 장비에 둔다.

### 성능 시험표

| 시험 | 크기 | batch | steps | 시간 | 최대 RAM/SWAP | 온도 | 성공 |
|---|---:|---:|---:|---:|---:|---:|---|
| 기준 | 512² | 1 | 20 | | | | |
| 낮은 steps | 512² | 1 | 12 | | | | |
| 큰 크기 | 768² | 1 | 20 | | | | |

성능 수치는 모델, JetPack, PyTorch, 냉각, 전력 모드에 따라 달라지므로 남의 결과 대신 자신의 장비에서 측정한다.

## 2. 모델/워크플로 변경 관리 템플릿

```text
Workflow name:
Workflow version:
ComfyUI commit/release:
Model filename + SHA-256:
Model license/source:
LoRA filename + SHA-256:
Custom nodes + version/commit:
Target: Windows / Jetson
Known memory limit:
Approved prompt template:
Reviewer:
Date:
```

## 3. 품질 검수 체크리스트

- [ ] 손가락, 얼굴, 제품 형상이 깨지지 않았는가?
- [ ] 의미 없는 글자·워터마크·서명이 생기지 않았는가?
- [ ] 상표, 저작권, 초상권 문제가 없는가?
- [ ] prompt와 결과가 업무 요구를 충족하는가?
- [ ] 같은 설정으로 다시 실행할 수 있는가?
- [ ] 원본과 생성물을 구분해 저장했는가?
- [ ] 자동 생성물임을 표시해야 하는 정책/법적 요구를 확인했는가?
