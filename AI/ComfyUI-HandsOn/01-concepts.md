# 01. ComfyUI 개념 이해

## 1. ComfyUI는 무엇인가

ComfyUI는 생성형 이미지 모델의 처리 과정을 **노드 그래프**로 조립하는 오픈소스 UI이자 실행 백엔드다. 일반 WebUI가 완성된 기능을 탭과 버튼으로 제공한다면, ComfyUI는 각 처리 단계를 블록처럼 연결한다.

```text
모델 불러오기 ─┬─> 긍정 프롬프트 ─┐
               ├─> 부정 프롬프트 ─┼─> 샘플링 ─> 잠재 이미지 해독 ─> 저장
빈 잠재 이미지 ────────────────────┘
```

그래프가 처음에는 복잡해 보이지만, 다음 장점이 있다.

- 실행 과정을 눈으로 확인할 수 있다.
- 중간 결과를 재사용해 불필요한 계산을 줄인다.
- 같은 설정과 seed를 저장해 재현하기 쉽다.
- ControlNet, LoRA, 업스케일, 영상 생성 등을 원하는 순서로 조합할 수 있다.
- API 형식 JSON으로 내보내 자동화 파이프라인에 연결할 수 있다.

## 2. 초보자가 알아야 할 용어

| 용어 | 쉬운 설명 | 비유 |
|---|---|---|
| Checkpoint | 그림을 만드는 핵심 모델 파일 | 화가의 두뇌와 화풍 묶음 |
| Node | 한 가지 일을 하는 블록 | 공장의 한 작업대 |
| Link | 노드 사이 데이터 연결 | 컨베이어 벨트 |
| Workflow | 노드와 링크 전체 구성 | 생산 공정 설계도 |
| Prompt | 만들고 싶은 내용을 적은 문장 | 작업 지시서 |
| Negative prompt | 피하고 싶은 특징 | 금지 사항 |
| Latent | 사람이 바로 볼 수 없는 압축된 이미지 표현 | 그림의 압축 설계도 |
| Sampler | 노이즈를 이미지로 바꾸는 반복 방법 | 그리는 순서/기법 |
| Steps | 샘플링 반복 횟수 | 다듬는 횟수 |
| CFG | 프롬프트를 얼마나 강하게 따를지 | 지시 준수 강도 |
| Seed | 최초 노이즈를 결정하는 숫자 | 같은 시작 재료 번호 |
| VAE | latent와 실제 이미지 사이 변환기 | 압축/해제 장치 |
| LoRA | 기본 모델에 작은 스타일·대상 지식을 추가 | 교체 가능한 보조 화풍 |
| ControlNet | 포즈, 선, 깊이 등 구조를 따라가게 하는 보조 모델 | 밑그림 자 |
| VRAM | 외장 GPU 전용 메모리 | GPU의 작업대 크기 |

## 3. 기본 text-to-image의 7개 노드

1. `Load Checkpoint`: checkpoint에서 MODEL, CLIP, VAE를 꺼낸다.
2. `CLIP Text Encode (Prompt)`: 긍정 문장을 모델이 이해하는 숫자로 바꾼다.
3. `CLIP Text Encode (Prompt)`: 부정 문장도 같은 방식으로 바꾼다.
4. `Empty Latent Image`: 출력 크기와 배치 수를 정한다.
5. `KSampler`: seed, steps, CFG, sampler, scheduler를 이용해 latent를 생성한다.
6. `VAE Decode`: latent를 눈으로 볼 수 있는 픽셀 이미지로 바꾼다.
7. `Save Image`: 결과를 `output` 폴더에 저장한다.

### 연결을 읽는 방법

- 노드 오른쪽 점은 출력, 왼쪽 점은 입력이다.
- 같은 데이터 형식끼리만 연결된다. 색상이 형식의 힌트다.
- 연결선을 따라가며 “이 입력은 어디서 왔는가?”를 묻는다.
- 빨간 노드는 필수 입력이나 모델 파일이 빠졌을 가능성이 크다.

## 4. 주요 설정의 시작값

SD 1.5 첫 실습의 안전한 시작값이다.

| 항목 | 시작값 | 바꾸면 생기는 일 |
|---|---:|---|
| Width × Height | 512 × 512 | 커질수록 메모리와 시간이 크게 증가 |
| Batch size | 1 | 커질수록 메모리 증가 |
| Steps | 20 | 너무 낮으면 거칠고, 높아도 항상 좋아지지는 않음 |
| CFG | 7 | 너무 높으면 과포화·왜곡 가능 |
| Sampler | `euler` 또는 `dpmpp_2m` | 질감과 수렴 특성이 달라짐 |
| Scheduler | `normal` 또는 `karras` | step별 노이즈 제거 분배가 달라짐 |
| Seed | 고정 정수 | 같은 조건 비교 시 반드시 고정 |

## 5. “같은 seed인데 왜 결과가 다르지?”

seed만 같다고 충분하지 않다. 아래가 모두 같아야 재현 가능성이 높다.

- checkpoint와 파일 해시
- 프롬프트 및 가중치
- 해상도, batch, steps, CFG
- sampler와 scheduler
- VAE, LoRA, ControlNet 및 강도
- ComfyUI/PyTorch/custom node 버전
- 하드웨어·정밀도·최적화 설정

Windows와 Jetson은 아키텍처, PyTorch 빌드, 연산 경로가 다르므로 **픽셀 단위 완전 동일성**을 기대하지 않는다. 시각적으로 동등한 결과와 반복 가능한 설정을 목표로 한다.

## 6. 모델 폴더 지도

```text
ComfyUI/models/
├─ checkpoints/   # SD 1.5, SDXL 등 checkpoint
├─ vae/           # 별도 VAE
├─ loras/         # LoRA
├─ controlnet/    # ControlNet 모델
├─ upscale_models/# ESRGAN 계열 업스케일 모델
├─ clip/          # 일부 모델의 text encoder
└─ unet/          # 일부 최신 모델의 diffusion model
```

모델마다 필요한 파일 구성이 다르다. “모든 `.safetensors`를 checkpoints에 넣기”는 잘못된 습관이다. 배포 페이지의 ComfyUI 설치 위치를 따른다.

## 7. 미니 확인 문제

- 해상도를 512에서 1024로 올리면 어떤 자원이 가장 먼저 부족해지는가?
- 두 sampler를 공정하게 비교하려면 무엇을 고정해야 하는가?
- `KSampler`의 출력이 곧 PNG 이미지가 아닌 이유는 무엇인가?
- 알 수 없는 커스텀 노드를 설치하는 것이 단순 JSON 파일을 여는 것보다 위험한 이유는 무엇인가?

정답: 대체로 GPU 메모리, seed와 나머지 조건, 출력이 latent이기 때문, 임의 Python 코드와 설치 스크립트를 실행할 수 있기 때문이다.
