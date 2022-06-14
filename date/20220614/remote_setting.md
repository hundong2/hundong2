#fatal: No configured push destination.
##error message 
```
$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>
```
현재 위치의 폴더가 깃허브의 원격 레포지토리랑 연결이 안되있다는 뜻이다.
깃허브에 있는 자신의 리모트 레포지토리 원격 저장소(origin)와 연동을 해야한다. 


git remote add <name> <url>
=> git remote add origin <원격 레포지토리 저장소 url>

정상적으로 깃허브 원격 저장소에 push 확인.
git push --set-upstream origin main
명령어를 해주면 정상적으로 깃허브 원격 저장소에 push된 것을 볼 수 있다

덤.
git init
-> 현재 로컬 폴더를 깃 로컬저장소로 만들어주는 명령어