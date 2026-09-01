## Contents

- [1. worktree](#1-worktree). 

## 1. Worktree

- 워크트리를 활용하여 새로운 기능을 개발하고 메인 브랜치에 병합하는 전체 과정을 실제 디렉토리(폴더) 경로 변화와 함께 설명합니다. 현재 원본 프로젝트가 `/Users/me/my-app` 경로에 있고 `main` 브랜치에 있다고 가정하겠습니다.

### 1. **새 브랜치 및 워크트리 동시 생성:** 프로젝트 내부가 아닌 상위 폴더(../)에 생성하는 것이 좋습니다..
현재 `my-app` 폴더에서 아래 명령어를 실행하여 `feature-login`이라는 새 브랜치를 만들면서 동시에 새 폴더를 생성합니다.

```bash
git worktree add -b feature-login ../my-app-login

```

* **경로 변화:** 기존 `/Users/me/my-app` (main 브랜치) 폴더 옆에 완전히 동일한 코드를 가진 `/Users/me/my-app-login` (feature-login 브랜치) 폴더가 새로 생겨납니다. 두 폴더는 서로 영향을 주지 않습니다.


### 2. **생성된 워크트리 폴더로 이동 및 작업:**
새로 만들어진 폴더로 이동하여 평소처럼 코드를 수정하고 커밋합니다.

```bash
cd ../my-app-login
# 파일 수정 작업 진행...
git add .
git commit -m "로그인 기능 추가"

```

* **경로 변화:** 파일 추가나 수정은 오직 `/Users/me/my-app-login` 폴더 내에서만 일어납니다. 원본 `my-app` 폴더에서 서버를 띄워두고 있었다면 아무런 방해 없이 계속 실행됩니다.


### 3. **작업 내역 통합 (Merge 또는 Push):**
작업을 마친 코드를 `main` 브랜치에 합쳐야 합니다. 상황에 따라 두 가지 방법 중 하나를 선택합니다.

### **방법 A: 로컬에서 바로 Merge (개인 프로젝트)**
원본 폴더로 돌아가서 방금 작업한 브랜치를 병합합니다.

```bash
cd ../my-app
git merge feature-login

```

### **방법 B: 원격 저장소에 Push 후 Pull Request (팀 협업)**
워크트리 폴더에서 바로 원격 저장소(GitHub 등)로 코드를 올립니다.

```bash
# my-app-login 폴더에서 실행
git push origin feature-login

```

이후 GitHub 웹사이트에서 `main` 브랜치로 병합(PR)을 진행합니다.


### 4. **워크트리 삭제 및 마무리:** 병합이 끝났다면 더 이상 워크트리 폴더를 유지할 필요가 없습니다..
원본 폴더(`/Users/me/my-app`)로 돌아와서 워크트리 폴더를 삭제하고, 필요 없어진 브랜치도 지워줍니다.

```bash
cd ../my-app

# 1. 워크트리(폴더) 연결 해제 및 삭제
git worktree remove ../my-app-login

# 2. 브랜치 삭제 (선택 사항)
git branch -d feature-login

```

* **경로 변화:** `/Users/me/my-app-login` 폴더가 컴퓨터에서 완전히 삭제되며, 다시 초기 상태인 `/Users/me/my-app` 폴더 하나만 깔끔하게 남게 됩니다.