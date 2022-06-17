GIT Submodule 
======
# Git Submodule 
부모 repo에서 하위 자식 repo를 관리하기 위한 것.
parent repo - child repo... 

## 1. Git submodule add

### first step 

```bash
git submodule add {submodule_repo_url}
or
git submodule add -b {branch_name} {submodule_repo_url}
```

### Second step
you'll check the file that named `.submodules`

submoudle file contents 
```bash
[submodue [file path]]
path = [file path]
url = [repo url]
```

you can add to branch name 
bellow example
```bash
[submodue [file path]]
path = [file path]
url = [repo url]
branch = [branch name]
```

### third step

```bash
git status #git status check 
git add . #add to local repo
git commit -m "{commit_message}" #commit to local repo
git push #push to origin 
```

## 2. git submodule update 

```bash
git submodule init
git submodule update 
```

## 3. git submodule clone from main repo

```bash
git clone --recurse-submodules {project_url}
```

## warnning 

if you clone main repo, then first clone main repo and then, child submodule get.
if you push main repo, then child submodule repo push and then, parent main repo push.  
<p>
There is one thing to note when applying submodules to a project. If changes are made to a submodule, you must push or pull before the main project. If you push/pull the main project and push/pull the submodule, an unexpected error may occur. This is because the main project does not have submodules as they are, but only stores path, url, and commit information.
</p>

site 
[Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules "submodule")



