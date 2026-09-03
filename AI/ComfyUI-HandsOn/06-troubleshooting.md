# 06. 문제 해결 가이드

문제를 만나면 무작정 재설치하지 말고 **증상 → 로그의 첫 원인 → 최소 구성 재현 → 한 번에 한 변경** 순서로 본다.

## 1. 공통 진단 순서

1. ComfyUI 콘솔의 마지막 한 줄만 보지 말고 첫 `ERROR`, `Traceback`, `CUDA` 오류부터 읽는다.
2. 오류 노드 이름과 node ID를 기록한다.
3. 기본 노드 + SD 1.5 + 512×512 + batch 1로 재현한다.
4. custom node를 모두 제외하면 정상인지 확인한다.
5. ComfyUI, PyTorch, GPU/JetPack, 모델 파일명을 기록한다.
6. 변경하기 전에 정상 workflow와 로그를 백업한다.

## 2. 증상별 해결표

| 증상 | 가능 원인 | 먼저 할 일 |
|---|---|---|
| 브라우저가 열리지 않음 | 서버 미실행/포트/방화벽 | 콘솔에 `8188` 주소가 떴는지 확인 |
| checkpoint가 `null` | 잘못된 폴더/확장자/새로고침 | `models/checkpoints` 확인 후 `R` 또는 재시작 |
| `CUDA out of memory` | 해상도·batch·모델이 큼 | 512², batch 1, preview off, lowvram |
| `Torch not compiled with CUDA` | 잘못된 PyTorch 설치 | Windows/Jetson에 맞는 빌드 재확인 |
| `Import Failed` custom node | 의존성/버전/아키텍처 문제 | 해당 노드만 비활성화하고 요구사항 확인 |
| 빨간 노드/unknown node | workflow의 custom node 누락 | 출처 검토 후 신뢰할 때만 설치 |
| 생성이 갑자기 매우 느림 | CPU fallback/swap/열 스로틀 | GPU 사용량, `tegrastats`, 전력/온도 확인 |
| 컨테이너 재시작 후 모델 소실 | volume 미마운트 | 호스트 폴더와 컨테이너 경로 점검 |
| 결과가 검정/이상한 색 | VAE 불일치/모델 손상 | 권장 VAE와 파일 해시 확인 |
| 같은 seed 결과가 다름 | 버전/정밀도/노드 차이 | 전체 재현 조건 비교 |

## 3. Windows 점검 명령

```powershell
nvidia-smi
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name,Id,WorkingSet64
Get-NetTCPConnection -LocalPort 8188 -ErrorAction SilentlyContinue
```

Portable Python의 CUDA 확인:

```powershell
cd D:\AI\ComfyUI_windows_portable
.\python_embeded\python.exe -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"
```

Windows의 전역 `python`이 아니라 Portable의 내장 Python으로 확인한다.

## 4. Jetson 점검 명령

```bash
cat /etc/nv_tegra_release
free -h
df -h
tegrastats
docker ps -a
docker logs --tail 200 <container_name_or_id>
```

컨테이너 안의 PyTorch 확인:

```bash
python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"
```

### Jetson에서 특히 확인할 것

- `aarch64`용 의존성인가?
- 현재 L4T와 컨테이너 태그가 맞는가?
- RAM과 swap이 가득 찼는가?
- NVMe/SD 저장 공간이 가득 찼는가?
- 전원 부족 또는 열 스로틀링이 있는가?
- models/output volume이 호스트에 연결됐는가?

## 5. custom node 이분 탐색

1. 종료한다.
2. 의심되는 custom node 폴더 이름에 `.disabled`를 붙이거나 Manager에서 비활성화한다.
3. 재시작한다.
4. 문제가 사라지면 그 노드와 의존성이 원인 후보다.
5. 여러 개라면 절반씩 비활성화해 범위를 줄인다.

커스텀 노드는 임의 코드를 실행할 수 있다. 오류를 없애기 위해 보안 수준을 낮추거나 알 수 없는 `pip install` 명령을 그대로 실행하지 않는다. [공식 custom node 보안 안내](https://docs.comfy.org/installation/install_custom_node)

## 6. 안전한 복구 전략

- 모델과 output을 삭제하지 않는다.
- 기존 설치 폴더를 덮어쓰지 않고 새 core 설치를 별도 폴더/컨테이너로 시험한다.
- 기본 workflow가 정상이면 custom node를 한 개씩 추가한다.
- 정상 조합의 버전/commit을 기록한다.
- Git을 쓴다면 workflow와 설정만 관리하고 대형 모델, output, 비밀키는 `.gitignore`에 둔다.

## 7. 도움 요청 시 포함할 정보

```text
OS / Windows build 또는 JetPack+L4T:
GPU / 장비:
설치 방식: Desktop / Portable / manual / container
ComfyUI version/commit:
PyTorch version + CUDA available:
모델 종류와 파일명(비밀 경로 제외):
재현 가능한 최소 workflow:
실행 명령:
전체 traceback:
이미 시도한 조치:
```
