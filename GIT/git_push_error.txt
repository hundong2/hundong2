 ```
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/xxx'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
-> git push origin +master 
기존 데이터의 손실을 막기 위해 푸시를 막음. 
