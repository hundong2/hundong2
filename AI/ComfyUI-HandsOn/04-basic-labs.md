# 04. 기초 실습

모든 실습은 결과 PNG와 workflow JSON을 함께 저장한다. 한 번에 하나의 값만 바꾸고, 비교할 때 seed를 고정한다.

## 실습 0. 기본 조작 익히기

### 목표

노드를 찾고 연결하고 삭제하며 workflow를 저장한다.

### 따라 하기

1. 빈 공간 더블클릭 또는 노드 검색 메뉴로 `Empty Latent Image`를 찾는다.
2. 노드를 드래그해 이동하고 휠로 확대/축소한다.
3. 노드의 출력 점에서 다른 노드 입력 점까지 드래그한다.
4. 노드를 선택해 삭제하고 `Ctrl+Z`로 복구한다.
5. workflow를 UI용 JSON으로 저장한다.
6. 메뉴에서 `Save (API Format)`을 찾아 API용 JSON도 저장한다. 메뉴가 없으면 설정의 개발자 옵션/API 저장 옵션을 확인한다.

API 형식의 구조를 먼저 보고 싶다면 [최소 API workflow 예제](examples/workflow_api_minimal.example.json)를 연다. placeholder checkpoint 이름을 자신의 실제 SD 1.5 파일명으로 바꿔야 실행된다.

### 확인

- UI용 JSON은 다시 편집할 그래프다.
- API용 JSON은 자동 실행용이며 `class_type`과 `inputs` 중심이다.

---

## 실습 1. 첫 text-to-image

### 목표

기본 7개 노드로 512×512 이미지를 생성한다.

### 설정

```text
Positive: a small friendly service robot reading a book in a quiet library,
          warm cinematic light, detailed digital illustration
Negative: blurry, low quality, deformed, extra fingers, text, logo, watermark
Size: 512 x 512
Batch: 1
Steps: 20
CFG: 7
Sampler: euler
Scheduler: normal
Seed: 20260902
```

### 절차

1. `Load Checkpoint`에서 SD 1.5 모델을 선택한다.
2. MODEL을 KSampler의 model에 연결한다.
3. CLIP을 긍정/부정 `CLIP Text Encode` 두 개에 연결한다.
4. 두 conditioning 출력을 KSampler의 positive/negative에 연결한다.
5. `Empty Latent Image`를 KSampler의 latent_image에 연결한다.
6. KSampler의 samples를 `VAE Decode` samples에 연결한다.
7. checkpoint의 VAE를 `VAE Decode` vae에 연결한다.
8. IMAGE를 `Save Image`에 연결하고 실행한다.
9. `lab01_txt2img_ui.json`과 `lab01_txt2img_api.json`을 저장한다.

### 관찰 기록

| 항목 | 기록 |
|---|---|
| 장비 | Windows / Jetson |
| 모델 파일명 | |
| 실행 시간 | |
| 최대 GPU/메모리 사용 | |
| 결과 파일 | |

---

## 실습 2. seed, steps, CFG 비교

### 목표

감으로 값을 바꾸지 않고 통제된 실험을 한다.

### 절차 A: seed

1. 실습 1의 모든 조건을 유지한다.
2. seed만 `11`, `22`, `33`으로 바꿔 세 장 생성한다.
3. 구도와 세부 요소가 어떻게 달라지는지 적는다.

### 절차 B: steps

1. 마음에 드는 seed 하나를 고정한다.
2. steps만 `10`, `20`, `30`으로 바꾼다.
3. 품질 향상과 시간 증가가 비례하는지 비교한다.

### 절차 C: CFG

1. seed와 steps를 고정한다.
2. CFG만 `4`, `7`, `10`으로 바꾼다.
3. 프롬프트 준수, 색 과포화, 형태 왜곡을 비교한다.

Jetson에서는 9장을 한꺼번에 queue에 넣기보다 한 장씩 실행하고 `tegrastats`를 기록한다.

---

## 실습 3. image-to-image

### 목표

입력 이미지의 구도를 유지하면서 스타일을 바꾼다.

### 추가 노드

- `Load Image`
- `VAE Encode`

### 연결 변경

```text
Load Image → VAE Encode → KSampler.latent_image
Checkpoint.VAE → VAE Encode.vae
```

### 설정

- 입력: 직접 촬영했거나 사용 권한이 있는 512×512 이미지
- prompt: `watercolor travel sketch, soft paper texture, gentle colors`
- denoise: 먼저 `0.35`, 다음 `0.65`
- 나머지는 고정

### 해석

- denoise가 낮으면 원본을 많이 유지한다.
- denoise가 높으면 프롬프트의 영향이 커지고 원본 구조가 변할 수 있다.

### 완료 기준

- 같은 seed에서 denoise 0.35/0.65 결과를 나란히 비교한다.
- 원본 이미지의 출처와 사용 권한을 기록한다.

---

## 실습 4. 부분 수정(inpainting)

### 목표

이미지 전체가 아니라 선택한 영역만 바꾼다.

### 예제 과제

책상 사진에서 컵 영역만 마스킹하고 `a small blue ceramic mug`로 바꾼다.

### 절차

1. `Load Image`로 이미지를 연다.
2. ComfyUI 마스크 편집기 또는 외부 편집기로 바꿀 영역을 흰색, 유지 영역을 검정으로 만든다.
3. inpainting workflow template를 불러온다.
4. 모델에 맞는 inpainting checkpoint/노드 구성을 확인한다.
5. 512×512, batch 1, denoise 0.5 전후에서 시작한다.
6. 마스크 경계가 보이면 마스크 blur/grow 값을 조금씩 조정한다.

### 실무 포인트

- 마스크를 너무 딱 맞게 칠하면 경계가 부자연스러울 수 있다.
- 제품 로고처럼 정확성이 필요한 부분은 생성 후 사람이 최종 검수한다.
- 업무 이미지 원본은 별도 보관하고 덮어쓰지 않는다.

---

## 실습 5. LoRA 적용

### 목표

기본 모델에 보조 스타일을 적용하고 강도를 비교한다.

### 준비

1. 기본 checkpoint와 호환되는 LoRA를 선택한다(SD 1.5용/SDXL용 혼동 금지).
2. 라이선스와 trigger word를 확인한다.
3. 파일을 `ComfyUI/models/loras`에 둔다.

### 노드

`Load LoRA`를 checkpoint와 text encode/KSampler 사이에 넣는다.

```text
Load Checkpoint.MODEL ─> Load LoRA.MODEL ─> KSampler
Load Checkpoint.CLIP  ─> Load LoRA.CLIP  ─> Text Encode 두 개
```

### 비교

- model strength: `0.4`, `0.7`, `1.0`
- clip strength: 우선 model strength와 동일
- seed, prompt, 나머지 설정 고정

강도가 높다고 항상 좋은 것은 아니다. 기본 모델의 해부학과 구도가 무너지는 지점을 찾는다.

---

## 실습 6. ControlNet 맛보기

### 목표

참조 이미지의 선 또는 포즈를 따르는 결과를 만든다.

### 권장 순서

1. 공식/신뢰할 수 있는 workflow template를 사용한다.
2. checkpoint 세대와 맞는 ControlNet 모델을 준비한다.
3. 첫 실습은 Canny edge처럼 이해하기 쉬운 전처리기를 쓴다.
4. control strength 0.5~0.8, 512×512, batch 1로 시작한다.
5. 전처리 결과를 Preview Image로 확인한다.

Jetson에서는 전처리 모델과 ControlNet이 메모리를 더 사용한다. Windows에서 먼저 완성한 뒤 노드를 최소화해 옮긴다.

---

## 실습 7. workflow 공유 테스트

### 목표

다른 장비에서 workflow를 재현한다.

1. Windows에서 실습 1 workflow를 저장한다.
2. 모델 파일명과 SHA-256을 기록한다.
3. Jetson에 같은 모델을 배치한다.
4. workflow JSON을 불러온다.
5. 누락 노드가 없는지 확인한다.
6. 512×512, batch 1로 실행한다.
7. 두 결과의 시간과 시각적 차이를 기록한다.

완전 동일한 픽셀보다 설정 이식 가능성과 운영 안정성을 평가한다.
