# Unix/Linux Version check

```bash
cat /proc/version
uname -a
cat /etc/issue
cat /etc/os-release
```

## uname option
uname의 주요한 옵션

-a, –all:
모든 시스템 정보를 출력합니다. 단, -p나 -i 정보가 없는 경우 생략합니다.
-s, –kernel-name:
s 옵션은 커널 이름을 출력합니다
-n, –nodename:
네트워크 호스트네임을 출력합니다.
-r, –kernel-release
r 옵션은 커널의 릴리스 버전을 출력합니다.
-v, –kernel-version
커널 버전을 출력합니다.
-m, –machine
m 옵션은 시스템의 하드웨어 아키텍처를 출력합니다.
-p, –processor
프로세서 타입을 출력합니다. 확인할 수 없는 경우 “unknown”을 출력합니다.
-i, –hardware-platform
하드웨어 플랫폼 정보를 출력합니다. 확인할 수 없는 경우 “unknown”을 출력합니다.
-o, –operating-system
o 옵션은 운영체제 이름을 출력합니다.
–help
도움말을 출력하고 종료합니다.
–version
버전 정보를 출력하고 종료합니다.

site :
[uname manpage](https://linux.die.net/man/1/uname "uname")