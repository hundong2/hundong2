# 02. Windows + NVIDIA GPU 설치

## 1. 설치 전 점검

PowerShell에서 다음을 실행한다.

```powershell
nvidia-smi
Get-CimInstance Win32_OperatingSystem | Select-Object Caption,OSArchitecture
Get-PSDrive -PSProvider FileSystem
```

확인할 것:

- `nvidia-smi`가 GPU 이름과 드라이버를 표시하는가?
- OS가 64비트인가?
- 설치 드라이브에 최소 30GB가 남았는가?

`nvidia-smi`가 없거나 오류라면 ComfyUI보다 NVIDIA 드라이버부터 해결한다.

## 2. 설치 방법 선택

### 방법 A: Desktop

일반 앱처럼 설치하고 환경 구성을 자동화하고 싶을 때 적합하다. 현재 Windows Desktop은 NVIDIA GPU 대상이며 베타 상태이므로 설치 과정은 바뀔 수 있다.

1. [공식 Windows Desktop 안내](https://docs.comfy.org/installation/desktop/windows)에서 설치 파일을 받는다.
2. GPU 선택에서 `NVIDIA GPU`를 고른다.
3. 모델을 저장할 충분한 공간이 있는 위치를 지정한다.
4. 초기화가 끝나면 앱을 실행한다.

### 방법 B: Portable — 이 교재의 기본 경로

Python을 따로 설치하지 않고 폴더 단위로 관리할 수 있다.

1. [공식 Portable 안내](https://docs.comfy.org/installation/comfyui_portable_windows)에서 받는다.
2. 최신 표준 NVIDIA Portable의 지원 GPU/드라이버 조건을 읽는다.
3. 구형 GPU라면 공식 페이지의 CUDA 12.6 + Python 3.12 대체 패키지를 고려한다.
4. 짧은 영문 경로에 압축을 푼다. 예: `D:\AI\ComfyUI_windows_portable`
5. `run_nvidia_gpu.bat`을 실행한다.
6. 콘솔을 닫지 말고 브라우저에서 `http://127.0.0.1:8188`을 연다.

대표 구조:

```text
ComfyUI_windows_portable/
├─ ComfyUI/
├─ python_embeded/
├─ update/
├─ run_nvidia_gpu.bat
└─ run_cpu.bat
```

> Portable의 Python은 `python_embeded\python.exe`다. 커스텀 노드 의존성을 Windows의 다른 Python에 설치하면 ComfyUI에서는 보이지 않는다.

## 3. 첫 모델 설치

초보 실습은 SD 1.5 FP16 checkpoint로 시작한다. 모델 배포 페이지에서 라이선스를 확인하고 `.safetensors` 파일을 다음 위치에 둔다.

```text
D:\AI\ComfyUI_windows_portable\ComfyUI\models\checkpoints\
```

ComfyUI에서 `R`을 눌러 목록을 새로 고치거나 서버를 재시작한다. `Load Checkpoint`의 드롭다운에서 모델을 선택한다.

## 4. 첫 실행

기본 workflow가 보인다면 다음 값을 확인한다.

- 512×512, batch 1
- steps 20, CFG 7
- seed는 임의의 고정 숫자
- 긍정 prompt: `a small friendly robot reading a book, warm desk lamp, detailed illustration`
- 부정 prompt: `blurry, low quality, text, watermark, deformed`

`Queue Prompt` 또는 `Ctrl+Enter`를 누른다. 결과는 기본적으로 `ComfyUI/output`에 저장된다.

## 5. 메모리가 부족할 때

Portable의 `run_nvidia_gpu.bat`을 복사해 `run_nvidia_lowvram.bat`으로 만들고 실행 줄에 옵션을 추가할 수 있다.

```bat
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --lowvram --preview-method none
pause
```

조치 순서:

1. batch를 1로 낮춘다.
2. 해상도를 512×512로 낮춘다.
3. 다른 GPU 사용 앱을 닫는다.
4. 미리보기를 끈다.
5. `--lowvram`을 사용한다.
6. 그래도 실패하면 더 작은 모델/워크플로를 쓴다.

## 6. LAN 접속(선택)

다른 기기에서 접속하려면 실행 줄에 `--listen`을 추가한다.

```bat
.\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build
pause
```

`ipconfig`로 Windows PC의 LAN IP를 확인하고 다른 기기에서 `http://PC_IP:8188`로 접속한다. Windows 방화벽은 **개인 네트워크에서만** 8188을 허용한다. 인증 없는 서버를 공용 Wi-Fi나 인터넷에 노출하지 않는다.

## 7. 업데이트와 복구

- 정상 workflow JSON을 먼저 백업한다.
- Portable은 `update\update_comfyui_stable.bat`을 우선 사용한다.
- 문제가 있을 때만 Python 의존성까지 갱신하는 스크립트를 고려한다.
- 업데이트 후 custom node가 깨지면 모든 custom node를 한꺼번에 재설치하지 말고 하나씩 확인한다.
- 완전 복구가 필요하면 기존 폴더를 보존한 채 새 Portable을 별도 폴더에 풀고 core workflow부터 시험한다.

## 8. 설치 완료 체크리스트

- [ ] `nvidia-smi`가 정상이다.
- [ ] `127.0.0.1:8188`이 열린다.
- [ ] checkpoint가 드롭다운에 보인다.
- [ ] 512×512 이미지 1장을 생성했다.
- [ ] workflow JSON을 `comfy-lab/workflows`에 저장했다.
- [ ] 결과 PNG와 사용한 모델/라이선스를 기록했다.
