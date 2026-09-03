# 참고 자료와 버전 기준

확인일: 2026-09-02. 설치 명령과 호환 조합은 변할 수 있으므로 실행 당일 공식 문서를 다시 확인한다.

## ComfyUI

- [ComfyUI 공식 GitHub](https://github.com/comfy-org/comfyui): 기능, 설치 방식, 지원 하드웨어
- [공식 시스템 요구사항](https://docs.comfy.org/installation/system_requirements): Python/PyTorch/하드웨어 안내
- [Windows Portable](https://docs.comfy.org/installation/comfyui_portable_windows): 다운로드, 실행, 모델 경로, LAN 접근
- [Windows Desktop](https://docs.comfy.org/installation/desktop/windows): Desktop 설치와 현재 베타 상태
- [첫 이미지 생성](https://docs.comfy.org/get_started/first_generation): checkpoint 위치와 기본 실행
- [Workflow JSON 규격](https://docs.comfy.org/specs/workflow_json): workflow JSON schema
- [서버 routes](https://docs.comfy.org/development/comfyui-server/comms_routes): `/prompt`, `/ws` 등 로컬 API
- [Custom node 설치와 보안](https://docs.comfy.org/installation/install_custom_node): 신뢰할 수 있는 노드만 설치해야 하는 이유
- [문제 해결](https://docs.comfy.org/troubleshooting/overview): low-VRAM과 진단 옵션

## NVIDIA Jetson

- [Jetson Orin Nano Developer Kit User Guide](https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/): 67 INT8 TOPS, 최대 102GB/s, 7~25W와 설치 가이드
- [JetPack 6.2.1](https://developer.nvidia.com/embedded/jetpack-sdk-621): 현재 교재의 기준 JetPack 계열
- [JetPack SDK 설치](https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/latest/setup_jetpack.html): `nvidia-jetpack` 설치와 버전 확인
- [Jetson PyTorch 설치](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/): JetPack 호환 PyTorch 빌드
- [Jetson PyTorch 호환표](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform-release-notes/pytorch-jetson-rel.html): PyTorch와 JetPack 조합
- [jetson-containers](https://github.com/dusty-nv/jetson-containers): JetPack/L4T별 컨테이너 자동 선택
- [jetson-containers ComfyUI 정의](https://github.com/dusty-nv/jetson-containers/tree/master/packages/cv/diffusion/comfyui): ARM64 이미지, 실행 방식, 기본 8188 포트

## 대안

- [Stable Diffusion WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)
- [AUTOMATIC1111 Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [InvokeAI](https://github.com/invoke-ai/InvokeAI)
- [Fooocus](https://github.com/lllyasviel/Fooocus): 공식 README의 제한적 LTS 상태 포함
- [SD.Next](https://github.com/vladmandic/sdnext)
- [Hugging Face Diffusers](https://github.com/huggingface/diffusers)
- [Diffusers pipeline 개요](https://huggingface.co/docs/diffusers/main/using-diffusers/pipeline_overview)
