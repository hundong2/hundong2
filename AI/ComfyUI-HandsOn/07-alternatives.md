# 07. 다른 인기 오픈소스와 프레임워크

“가장 좋은 도구”보다 **사용 목적, 모델 지원, 하드웨어, 라이선스, 프로젝트 활동 상태**가 중요하다.

## 1. 비교표

| 도구 | 형태 | 강점 | 이런 사람에게 | Jetson 관점 |
|---|---|---|---|---|
| [ComfyUI](https://github.com/comfy-org/comfyui) | 노드 UI + API | 복잡한 파이프라인, 재사용, 자동화 | 워크플로를 세밀하게 설계 | 컨테이너/ARM 의존성 검증 필요 |
| [Stable Diffusion WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) | 탭 기반 WebUI | 익숙한 A1111 계열 UI, 자원 관리/실험 기능 | 노드보다 폼 UI를 선호 | ARM 공식 경로가 약해 직접 검증 필요 |
| [AUTOMATIC1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 탭 기반 WebUI | 방대한 사용 경험과 확장 생태계 | 전통적인 SD UI 학습 | Jetson에서는 버전/확장 호환 부담 |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | 캔버스 + workflow | Unified Canvas, 편집 중심 UX, 모델 관리 | 디자이너·콘텐츠 팀 | 요구 사양과 ARM 지원을 릴리스별 확인 |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | 단순 WebUI | 적은 설정으로 SDXL 이미지 생성 | prompt에 집중하는 입문자 | 8GB 통합 메모리에 SDXL 부담; 제한 LTS 상태 |
| [SD.Next](https://github.com/vladmandic/sdnext) | 통합 WebUI + REST API | 다양한 백엔드/모델과 API | 여러 하드웨어를 실험 | jetson-containers 패키지 존재, 조합 검증 필요 |
| [Hugging Face Diffusers](https://github.com/huggingface/diffusers) | Python 라이브러리 | 코드, 테스트, 서비스 통합, 다양한 pipeline | 개발자·연구자·제품 백엔드 | UI보다 코드 최적화/배포에 유리 |

## 2. 도구별 설명

### Stable Diffusion WebUI Forge

A1111 계열 사용법을 유지하면서 자원 관리와 최신 모델 실험에 초점을 둔다. txt2img/img2img를 폼 방식으로 빠르게 쓰고 싶을 때 편하다. 확장 프로그램은 프로젝트와 버전 호환을 확인한다.

### AUTOMATIC1111 Stable Diffusion WebUI

오랫동안 널리 쓰인 Gradio 기반 UI로 관련 튜토리얼과 확장이 많다. 노드 연결 없이 기능별 탭을 쓰고 싶은 입문자에게 이해하기 쉽다. 다만 공식 저장소의 릴리스/활동과 사용하려는 최신 모델 지원을 확인한 뒤 선택한다.

### InvokeAI

이미지 생성뿐 아니라 캔버스에서 영역 선택, in/outpainting, 반복 편집하는 창작 흐름에 강하다. 노드 workflow도 제공한다. 팀의 아티스트가 직접 편집할 경우 ComfyUI보다 UX가 잘 맞을 수 있다.

### Fooocus

복잡한 설정을 감추고 prompt와 이미지에 집중하도록 만든 SDXL 중심 도구다. 공식 저장소는 현재 새로운 모델 아키텍처를 적극 추가하기보다 제한적 LTS/버그 수정 상태라고 밝히므로 이 점을 알고 선택한다.

### SD.Next

다양한 모델/백엔드와 REST API를 지향하는 통합 WebUI다. 여러 GPU 백엔드를 실험하거나 A1111 스타일 UI와 API가 함께 필요할 때 후보가 된다.

### Hugging Face Diffusers

UI가 아니라 Python 라이브러리다. `DiffusionPipeline` 계열로 모델, scheduler, ControlNet 등을 코드로 구성한다. 단위 테스트, 배치 처리, 서비스 API, 제품 코드에 통합할 때 ComfyUI JSON보다 코드 기반 구성이 더 자연스러울 수 있다. [공식 pipeline 설명](https://huggingface.co/docs/diffusers/main/using-diffusers/pipeline_overview)

## 3. 목적별 추천

| 목적 | 1순위 후보 | 이유 |
|---|---|---|
| 생성형 이미지 원리와 파이프라인 학습 | ComfyUI | 데이터 흐름이 보임 |
| 처음 한 장을 가장 단순하게 생성 | Fooocus 또는 Forge | 설정 진입장벽이 낮음 |
| 캔버스 기반 반복 편집 | InvokeAI | 편집 UX 중심 |
| 기존 SD 튜토리얼/확장 활용 | A1111/Forge | 자료와 친숙한 UI |
| 백엔드 서비스 개발 | Diffusers 또는 ComfyUI API | 코드 또는 workflow 자동화 |
| Jetson에서 빠른 첫 성공 | jetson-containers가 제공하는 ComfyUI/SD.Next 패키지 검토 | JetPack 호환 구성을 자동 선택 가능 |
| 복잡한 제작 workflow 공유 | ComfyUI | JSON 그래프 공유와 노드 조합 |

## 4. 선택 전에 확인할 8가지

1. 저장소의 최근 commit/release와 미해결 주요 이슈
2. 라이선스(도구뿐 아니라 모델/LoRA/출력 사용 조건)
3. 원하는 모델 아키텍처 지원 여부
4. Windows x86-64 또는 Jetson ARM64 지원 여부
5. 필요한 VRAM/RAM과 실제 장비 벤치마크
6. extension/custom node의 신뢰성과 유지 상태
7. API, queue, 인증, 배포 방식
8. workflow/metadata의 재현성과 이전 가능성

## 5. 학습 권장 경로

초보자는 ComfyUI로 기본 원리를 익힌 다음, 목적에 따라 한 도구만 추가한다.

- 창작/편집 비중이 크면 InvokeAI
- 간단한 폼 UI가 필요하면 Forge
- 제품 코드와 테스트가 중요하면 Diffusers
- 최소 설정 SDXL 체험이면 Fooocus(제한 LTS 상태 고려)

여러 UI를 동시에 설치하면 모델 중복과 Python 의존성 충돌이 생기기 쉽다. 공용 모델 경로를 구성할 때는 각 도구가 기대하는 폴더 종류를 정확히 매핑하고, 업데이트 전 백업한다.
