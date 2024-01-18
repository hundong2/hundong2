---
title: "Inside VisionOS: 18 things developers need to know about coding for Apple Vision Pro"
permalink: /posts/AppleVisionPro/
excerpt: "Apple Vision Pro 코딩 시 개발자가 알아야 할 것들"
redirect_from:
  - /theme-setup/
categories:
  - AppleVisionPro
tags:
  - AppleVisionPro
toc: true
---

# [출처: geeknews - Apple Vision Pro 코딩 시 개발자가 알아야 할 것들 (zdnet.com)](https://news.hada.io/topic?id=12866)  
- https://www.zdnet.com/article/inside-visionos-18-things-developers-need-to-know-about-coding-for-apple-vision-pro/  


- VisionOS 개발에 사용되는 도구와 라이브러리는 많은 Apple 개발자들에게 이미 익숙함  
- VisionOS는 iOS 및 iPad OS 개발의 확장으로, SwiftUI와 UIKit을 사용해 사용자 인터페이스를 구축하며, RealityKit은 3D 콘텐츠와 애니메이션을 표시하는 데 사용됨  
- 모든 앱은 3D 공간에서 존재해야 하며, 기존의 2D 앱도 공간에서 "떠다니는" 형태로 표시됨  
- VisionOS는 Xcode 개발자들에게 아이폰/아이패드/맥 외의 새로운 데스티네이션을 제공하며, 앱을 재빌드하면 VisionOS의 기능이 추가됨  
- 기존의 UIKit 앱도 VisionOS용으로 재컴파일 가능하며, VisionOS의 하이라이트 및 3D 프레즌스 기능을 얻을 수 있음  
- 전통적인 UI 요소는 새로운 Z-offset 옵션을 통해 3D 공간으로 푸시될 수 있음  
- VisionOS는 눈 추적을 사용하여 Dynamic Foveabtion(이미지의 특정 영역이 다른 영역보다 더 세밀하게 표현되는 이미지 처리 기법)을 가능하게 함  
- 객체 조명은 현재 공간 조건을 따름(사용자가 헤드셋을 착용하고 있는 공간의 조명 및 그림자 특성을 얻게됨)  
- ARKit은 실제 방의 모델을 앱에 제공하며, 평면 추정, 장면 재구성, 이미지 앵커링 기능을 포함함  
- VisionOS의 ARKit은 골격 손 추적 및 접근성 기능을 추가함. 사용자는 손의 움직임뿐만 아니라 눈의 움직임, 음성, 머리의 움직임과도 상호작용가능  
- Unity는 RealityKit 위에 레이어로 추가되어 Unity 개발자들이 VisionOS를 직접 타겟팅할 수 있음  
- Reality Composer Pro는 3D 콘텐츠를 미리보고 준비하기 위한 새로운 개발 도구  
- Shared-Space(공유 공간) 처리는 기기 내에서 이루어지며, 3D 매핑에는 클라우드 프로세싱이 사용되지 않음  
- 장치가 없는 경우, Xcode는 미리보기 및 시뮬레이터를 제공함  
- Vision Pro를 소유한 경우, 가상 공간에서 전체 코딩이 가능함. Mac 데스크톱을 가상 공간으로 확장하므로 Xcode 개발 환경을 Vision Pro 앱과 나란히 사용할 수 있음  
- Vision Pro 전용 앱 스토어가 있으며, 앱과 인앱 구매가 가능  
- Apple은 코딩 지원 자원을 제공하며, 개발자들은 런던, 뮌헨, 상하이, 싱가포르, 도쿄, 쿠퍼티노에 설치한 Apple Vision Pro 개발자 랩을 이용할 수 있음  
- 개발자들은 Vision Pro 앱 스토어에 앱을 제출할 수 있으며, 앱을 증강 현실(AR), 가상 현실(VR), 확장 현실(XR) 또는 혼합 현실(MR)로 설명하는 것 대신 "Spatial Computing  (공간 컴퓨팅)" 앱으로 설명해야 함.  