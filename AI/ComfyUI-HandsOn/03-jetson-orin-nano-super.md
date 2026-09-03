# 03. Jetson Orin Nano Super 설치와 운영

## 1. Windows와 무엇이 다른가

| 항목 | Windows + 외장 NVIDIA GPU | Jetson Orin Nano Super |
|---|---|---|
| CPU 아키텍처 | 보통 x86-64 | ARM64(aarch64) |
| GPU 메모리 | 시스템 RAM과 분리된 VRAM | CPU/GPU가 8GB LPDDR5 통합 메모리 공유 |
| 설치 패키지 | Desktop/Portable 사용 가능 | Windows Portable 사용 불가 |
| PyTorch | 일반 CUDA wheel | JetPack 호환 Jetson 빌드/컨테이너 필요 |
| 저장 장치 | 대용량 SSD가 일반적 | NVMe 권장, SD카드는 병목·용량 주의 |
| 냉각/전력 | 데스크톱 여유가 큼 | 7~25W 모드, 전원·팬·스로틀링 중요 |
| 권장 역할 | 설계, 고해상도, 복잡한 생성 | 경량 추론, 현장 배치, API 실행 |

Orin Nano Super는 최대 67 INT8 TOPS, 8GB 통합 메모리, 최대 102GB/s 대역폭을 제공하지만, 이 숫자를 데스크톱 GPU의 생성 속도나 VRAM 용량과 직접 비교하면 안 된다. 확산 모델은 메모리 크기와 PyTorch 연산 지원의 영향을 크게 받는다. [NVIDIA 공식 사양](https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/)

## 2. 이 교재의 권장 방식

Jetson에서 PyTorch와 CUDA 조합을 수동으로 맞추는 것은 초보자에게 오류가 많다. 기본 경로는 JetPack/L4T에 맞는 이미지를 찾는 [jetson-containers](https://github.com/dusty-nv/jetson-containers)다. 이 프로젝트는 ComfyUI용 ARM64 컨테이너 정의와 `autotag`를 제공한다.

> 커뮤니티 프로젝트이므로 NVIDIA/ComfyUI의 공식 제품 지원과는 다르다. 배포 전에는 이미지 태그, 구성 파일과 보안 업데이트를 직접 검토한다.

## 3. JetPack과 하드웨어 준비

1. 중요한 파일을 백업한다.
2. [JetPack 6.2.1 공식 페이지](https://developer.nvidia.com/embedded/jetpack-sdk-621)와 보드 가이드에 따라 SD 이미지 또는 SDK Manager로 설치한다.
3. 구형 펌웨어 보드는 JetPack 6.x 부팅 전에 펌웨어 갱신이 필요할 수 있으므로 공식 설치 경로를 따른다.
4. NVMe SSD, 정격 전원, 팬을 준비한다.

부팅 후 확인:

```bash
uname -m
cat /etc/nv_tegra_release
apt list --installed 2>/dev/null | grep nvidia-jetpack
df -h
free -h
nvidia-smi 2>/dev/null || true
```

정상 기대값:

- 아키텍처는 `aarch64`
- L4T/JetPack 버전이 표시됨
- 모델과 컨테이너를 둘 저장 공간이 충분함

필요한 JetPack 구성 요소가 빠졌다면 공식 가이드에 따라 설치한다.

```bash
sudo apt update
sudo apt install nvidia-jetpack
```

## 4. 성능 모드와 냉각

지원되는 모드를 먼저 조회한다.

```bash
sudo nvpmodel -q
sudo nvpmodel -q --verbose
```

모드 ID는 JetPack과 구성에 따라 다를 수 있으므로 인터넷 예제의 숫자를 그대로 복사하지 않는다. `/etc/nvpmodel.conf` 또는 조회 결과에서 25W/MAXN SUPER에 해당하는 ID를 확인한 뒤 적용한다.

```bash
sudo nvpmodel -m <확인한_모드_ID>
sudo jetson_clocks
```

모니터링:

```bash
tegrastats
```

온도 상승, `RAM`/`SWAP`, CPU/GPU 사용량을 본다. `jetson_clocks`는 소비 전력과 발열을 높일 수 있다. 안정적인 전원과 냉각 없이 무조건 최대 성능으로 두지 않는다.

## 5. NVMe와 Docker 공간

컨테이너가 수 GB이고 모델도 크므로 Docker data-root와 모델 캐시는 NVMe에 두는 것이 좋다. 기존 Docker 데이터가 있다면 임의로 이동하지 말고 Docker 공식 절차에 따라 백업·마이그레이션한다. 초보자는 처음부터 NVMe에 OS를 설치하는 편이 안전하다.

현재 저장 위치 확인:

```bash
docker info | grep "Docker Root Dir"
df -h
```

## 6. jetson-containers 설치

```bash
sudo apt update
sudo apt install -y git
git clone https://github.com/dusty-nv/jetson-containers.git
cd jetson-containers
bash install.sh
```

터미널을 다시 열고 호환 이미지 탐색을 확인한다.

```bash
autotag comfyui
```

`autotag`는 현재 JetPack/L4T와 맞는 이미지를 찾고, 없으면 빌드를 제안할 수 있다. 빌드는 오래 걸리고 저장 공간을 많이 사용한다. 출력되는 이미지 태그와 대상 L4T가 맞는지 확인한다.

## 7. ComfyUI 실행

먼저 모델과 입출력용 호스트 폴더를 만든다.

```bash
mkdir -p "$USER/comfy-data/models" "$USER/comfy-data/input" "$USER/comfy-data/output"
```

가장 단순한 첫 실행:

```bash
jetson-containers run $(autotag comfyui)
```

현재 ComfyUI 컨테이너 정의는 기본적으로 `0.0.0.0:8188`에서 서버를 시작한다. 같은 LAN의 PC 브라우저에서 다음으로 접속한다.

```text
http://JETSON_IP:8188
```

Jetson IP 확인:

```bash
hostname -I
```

데이터를 영속화하려면 컨테이너 내부의 실제 ComfyUI 경로(`/opt/ComfyUI`)를 기준으로 폴더를 마운트한다.

```bash
jetson-containers run \
  --volume "$USER/comfy-data/models:/opt/ComfyUI/models" \
  --volume "$USER/comfy-data/input:/opt/ComfyUI/input" \
  --volume "$USER/comfy-data/output:/opt/ComfyUI/output" \
  $(autotag comfyui)
```

처음에는 빈 models 전체를 마운트하면 이미지에 포함된 기본 디렉터리를 가릴 수 있다. 문제가 생기면 `checkpoints`, `loras`처럼 하위 폴더별로 마운트한다.

## 8. 첫 모델과 권장 설정

Jetson 8GB에서는 아래부터 시작한다.

- SD 1.5 FP16 checkpoint
- 512×512
- batch 1
- steps 15~20
- preview 없음 또는 최소화
- 기본 노드만 사용

대형 SDXL/FLUX, 여러 ControlNet, 고해상도 fix, 큰 batch, 영상 모델은 메모리 부족이나 긴 실행 시간이 발생하기 쉽다. 가능 여부와 “실무적으로 쓸 만한 속도”는 다른 문제다.

모델을 호스트에 받은 뒤:

```bash
ls -lh "$USER/comfy-data/models/checkpoints"
sha256sum "$USER/comfy-data/models/checkpoints/모델파일.safetensors"
```

브라우저에서 `R`로 새로 고치거나 컨테이너를 재시작한다.

## 9. 메모리 부족 대응

통합 8GB는 OS, 브라우저, Docker, CPU, GPU가 함께 쓴다.

1. Jetson에서는 브라우저를 닫고 다른 PC에서 UI에 접속한다.
2. 512×512, batch 1로 낮춘다.
3. SD 1.5와 기본 VAE를 쓴다.
4. 미리보기와 불필요한 custom node를 끈다.
5. 한 번에 하나의 작업만 실행한다.
6. 메모리 누수가 의심되면 프로세스/컨테이너를 재시작한다.
7. swap은 비상 완충장치일 뿐 GPU 메모리를 빠르게 만들어 주지 않는다. NVMe swap 과다 사용은 매우 느리다.

컨테이너 실행 명령을 덮어쓸 때는 이미지의 기본 명령과 경로를 확인한 후 다음과 같은 저메모리 옵션을 쓸 수 있다.

```bash
python3 /opt/ComfyUI/main.py --listen 0.0.0.0 --port 8188 --lowvram --preview-method none
```

## 10. Windows에서 설계하고 Jetson에서 실행하는 흐름

```text
Windows: workflow 작성 → 모델/노드 최소화 → API JSON 저장
     ↓ 같은 파일 이름과 폴더 구조 준비
Jetson: 512px·batch 1 검증 → tegrastats 기록 → API 서비스로 반복 실행
```

이식 체크리스트:

- [ ] 모델 파일명과 SHA-256이 같다.
- [ ] Jetson ARM64에서 모든 custom node 의존성이 설치 가능한가?
- [ ] API JSON에 Windows 절대 경로가 없는가?
- [ ] 1회 실행 전후 `tegrastats`를 기록했는가?
- [ ] 전원 재부팅 후에도 모델/출력 볼륨이 유지되는가?
- [ ] LAN 외부에서 8188에 접근할 수 없게 막았는가?

## 11. 수동 설치를 기본으로 하지 않는 이유

Jetson용 PyTorch는 JetPack 버전에 맞는 NVIDIA 빌드가 필요하고, 일부 custom node는 x86-64 전용 wheel 또는 CUDA 확장 빌드를 요구한다. 일반 PC용 `pip install torch` 명령을 그대로 쓰면 CPU 빌드가 설치되거나 호환 오류가 날 수 있다. 수동 설치가 필요하다면 [NVIDIA의 Jetson PyTorch 설치 문서](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/)와 [호환표](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform-release-notes/pytorch-jetson-rel.html)를 먼저 확인하고 별도 venv에서 시험한다.
