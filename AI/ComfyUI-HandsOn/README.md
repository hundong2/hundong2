# ComfyUI 초보자 실습 가이드

> 기준일: 2026-09-02<br>
> 대상: Windows 10/11 + NVIDIA GPU, NVIDIA Jetson Orin Nano Super Developer Kit<br>
> 목표: 설치에서 끝나지 않고, 재현 가능한 이미지 생성 워크플로와 간단한 자동화까지 직접 만들어 본다.

## 1. 이 가이드에서 배우는 것

- ComfyUI의 노드, 링크, 워크플로, 모델, seed가 무엇인지 설명할 수 있다.
- Windows와 Jetson에서 각자 맞는 방법으로 ComfyUI를 실행한다.
- text-to-image, image-to-image, inpainting, ControlNet, LoRA를 단계별로 실습한다.
- 워크플로를 JSON으로 저장하고 API로 반복 실행한다.
- VRAM/통합 메모리 부족, 모델 미인식, 커스텀 노드 오류를 진단한다.
- ComfyUI 외의 도구를 목적에 맞게 선택한다.

## 2. 추천 학습 순서

| 순서 | 문서 | 예상 시간 | 완료 기준 |
|---:|---|---:|---|
| 1 | [개념 이해](01-concepts.md) | 30분 | 기본 노드 7개의 역할을 말할 수 있다 |
| 2A | [Windows 설치](02-windows-setup.md) | 30~60분 | 브라우저에서 `127.0.0.1:8188` 접속 |
| 2B | [Jetson 설치](03-jetson-orin-nano-super.md) | 1~3시간 | 다른 PC에서 Jetson의 8188 포트 접속 |
| 3 | [기초 실습](04-basic-labs.md) | 2~4시간 | 실습 1~5 결과와 workflow JSON 저장 |
| 4 | [실무 레시피](05-production-recipes.md) | 2~4시간 | 배치 생성 또는 제품 이미지 편집 완료 |
| 5 | [문제 해결](06-troubleshooting.md) | 필요할 때 | 증상→원인→조치 순으로 진단 |
| 6 | [대안 비교](07-alternatives.md) | 20분 | 자신의 목적에 맞는 도구 선택 |

Windows만 있다면 2A로, Jetson만 있다면 2B로 이동하면 된다. 두 장비가 모두 있다면 **Windows에서 워크플로를 설계하고 Jetson에서 경량 워크플로를 실행**하는 방식이 가장 실용적이다.

## 3. 준비물

### 공통

- 여유 저장 공간 30GB 이상(모델을 여러 개 쓰면 100GB 이상 권장)
- 안정적인 인터넷 연결
- Chrome/Edge 계열 최신 브라우저
- 모델 라이선스와 사용 범위를 확인하는 습관

### Windows

- Windows 10/11 64비트
- NVIDIA GPU와 최신 드라이버
- VRAM 6GB 이상 권장. 4GB도 SD 1.5 저해상도 실습은 가능하지만 제약이 크다.
- 압축 해제 도구(7-Zip 권장)

### Jetson Orin Nano Super

- Jetson Orin Nano Super Developer Kit(8GB)
- JetPack 6.2 계열
- 충분한 전원 공급과 능동 냉각
- microSD보다 NVMe SSD 권장(컨테이너와 모델 I/O가 많음)
- 같은 LAN에 연결된 별도 PC 권장(PC 브라우저에서 UI 사용)

## 4. 빠른 결정표

| 상황 | 권장 시작점 |
|---|---|
| Windows 초보자, 빨리 체험 | ComfyUI Desktop 또는 NVIDIA Portable |
| Windows에서 폴더째 백업·이동 | Portable |
| Python 환경을 직접 통제 | Manual install + venv |
| Jetson에서 안정적으로 시작 | `jetson-containers`의 ComfyUI 컨테이너 |
| 8GB Jetson에서 첫 모델 | SD 1.5 FP16, 512×512, batch 1 |
| 고급 워크플로 설계 | VRAM이 큰 Windows PC |
| 현장/엣지 반복 실행 | Windows에서 검증 후 Jetson API로 배포 |

## 5. 실습 결과물 폴더 규칙

아래 구조를 장비별로 만들어 두면 복구와 비교가 쉽다.

```text
comfy-lab/
├─ workflows/       # UI용 JSON과 API용 JSON
├─ inputs/          # 원본 이미지, 마스크, 포즈 이미지
├─ outputs/         # 생성 결과
├─ models-notes/    # 모델 URL·라이선스·해시 기록
└─ logs/            # 오류 로그와 성능 측정 기록
```

모델 파일 자체는 Git에 커밋하지 않는다. workflow JSON에 개인 경로나 비밀키가 들어 있지 않은지도 확인한다.

## 6. 가장 중요한 안전 수칙

1. 모델은 공식 배포처나 신뢰할 수 있는 저장소에서 받고 가능하면 `safetensors` 형식을 사용한다.
2. 커스텀 노드는 Python 코드를 실행한다. 설치 전에 저장소, 최근 활동, 이슈, `requirements.txt`, `install.py`를 확인한다.
3. `--listen 0.0.0.0`은 LAN에 서버를 공개한다. 공유기 포트포워딩으로 인터넷에 직접 노출하지 않는다.
4. 업무용 결과물은 모델·LoRA·입력 이미지의 라이선스와 개인정보/초상권을 별도로 검토한다.
5. 업데이트 전에는 정상 동작하는 workflow, ComfyUI 버전, custom node 버전을 기록한다.

## 7. 공식 자료

- [ComfyUI 공식 문서](https://docs.comfy.org/)
- [ComfyUI 공식 GitHub](https://github.com/comfy-org/comfyui)
- [Windows Portable 설치](https://docs.comfy.org/installation/comfyui_portable_windows)
- [Jetson Orin Nano 개발 키트 가이드](https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/)
- [JetPack 6.2.1](https://developer.nvidia.com/embedded/jetpack-sdk-621)
- [Jetson용 컨테이너 프로젝트](https://github.com/dusty-nv/jetson-containers)

버전과 다운로드 방식은 자주 바뀐다. 명령을 실행하기 전에 위 공식 페이지의 현재 지원 조합을 한 번 더 확인한다.
