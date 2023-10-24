# Linux command reference page

## 1. SCP Command ( Local <-> Server ) File Transfer

- means : Secure Copy
- ssh 원격 접속 프로토콜 기반, ssh와 동일한 22번 포트 사용
- local <-> remote, remote <-> remote 모두 사용 가능

### 1.1 Usage

```
scp [option] [source] [target]
```

```sh
usage: scp [-346BCpqrTv] [-c cipher] [-F ssh_config] [-i identity_file]
            [-J destination] [-l limit] [-o ssh_option] [-P port]
            [-S program] source ... target
```

### 1.2 option

- `-r` : 폴더 내 내용들을 재귀적으로 copy
- `-P` : Port 지정
- `-i` : 인증서 파일을 이용하여 사용
