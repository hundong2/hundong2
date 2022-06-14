# Git Clone unrelated histories error 
## error message 
```
From https://github.com/[repo name]
 * branch            master     -> FETCH_HEAD
fatal: refusing to merge unrelated histories
```

## doing 
- 신규로 만든 프로젝트와 기존에 있는 프로젝트는 공통 적으로 같은 조상을 보고 있지 않아서 서로 다른 프로젝트라고 인식 함.
- 따라서 독립적인 두 프로젝트를 병합하기 위해 아래의 command 사용
```
git pull origin [branch name] --allow-unrelated-histories
```