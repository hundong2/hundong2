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

## 2. Linux Log 파일 종류 및 분석

1. Log File 소개

- 컴퓨터 시스템의 모든 사용내역을 기록하고 있는 파일을 의미 한다.
- 컴퓨터 시스템에 해킹사고가 발생할 경우 로그파일을 근거로 사고원인과 해커를 추적 한다.
- 로그파일 자체가 해커의 의해 삭제되면 추적 자체가 불가능하게 되므로 로그파일 보호 필요

1.  Linux / Unix Log File

- Linux / Unix 대부분의 로그 파일 저장 경로는 "/var/log"에 저장 (위치 변경 가능)
- Linux log 파일은 일반적으로 텍스트 형식으로 저장
- 텍스트 형식의 log 파일 : (cat , less) 명령어, vi 편집기를 통하여 내용 확인 가능
- 텍스트 형식이 아닌 log 파일(바이너리 형식) : btmp 및 wtmp log는 텍스트 형식이 아니라서 cat , less 및 vi 편집기로 하려고 하면 글씨가 깨져서 나오기 때문에 특정 명령어를 쳐야 확인이 가능하다.
- 시스템과 관련된 데몬은 syslogd / klogd 들이 존재 한다.

2.  Windows Log File

- 윈도우는 로그 대신 이벤트라는 정보를 시스템 운영 전반에 걸쳐서 저장 한다.(이벤트 로그)
- 기본 이벤트는 시스템에서 발생한 모든 이벤트의 상황들을 저장하는 응용 프로그램 이벤트, 보안 이벤트, 시스템 이벤트가 존재 한다.
- IIS 서버를 운영하는 경우 웹, FTP 로그가 따로 존재 한다.

1. Linux Log File

2)  로그 관련 데몬
    ① 로그 데몬
    ▶ syslogd - 커널과 여러 가지 시스템 프로그램은 각종 에러와 경고 메시지, 기타 일반적인 메시지들을 출력하는데 syslogd는 메시지들을 파일로 기록하는 데몬 이다.
    ▶ klogd - 부팅 후에 부팅과 관련된 메시지를 보기 위해서는 dmesg 명령어를 사용 한다.
    (실제 /var/log/dmesg 라는 파일의 정보를 가지고 오는 것이 아니다.) - 시스템에는 부팅과 관련된 메시지를 포함하여 커널 관련 메시지를 담는 약 8196 byte의 버퍼 크기를 갖고 메시지를 기록하는데 이 메시지를 기록하는 것이 klogd 데몬
    ② 관련 파일

    - /etc/rc.d/init.d/syslog : 실행과 관련된 시크립트 파일로 실질적인 실행파일 syslogd와 klogd 데몬을 모두 실행시킨다.
    - /etc/syslog.conf : syslog 데몬의 환경설정 파일
    - /etc/sysconfig/syslog : syslogd/klogd의 시작과 관련된 스크립트의 환경 파일 이다.

1)  /etc/syslog.conf 파일 분석

- syslog.conf 파일은 시스템 로그데몬 'syslogd' 이 실행이 될때 참조되는 로그설정 파일로써 관련된 로그파일들이 어떤 경우에 어떤 파일에 남겨지는가에 대하여 정의 한다.
  ① 기본 구성형식

  - selector field와 action field 두 필드로 구성
  - selector field(선택자 필드) : 어떤 것을 기록할 것인가 설정하는 부분이다.
  - action field(액션 필드) : 어느파일에 로그를 기록할 것인가를 설정하는 부분이다.
  - 선택자 필드에는 메시지 종류(facility)와 메시지 우선 순위(priority) 지정이 가능하다.
  - 액션 필드에는 선택자 필드에서 설정한 메시지들이 전달될 곳을 지정 한다. ( 콘솔, 파일명, 사용자 또는 원격 시스템이 사용 될 수 있는 값)

② 메시지 종류 (facility) - 메시지를 발생시키는 포로그램의 유형을 나타낸다. - facility의 종류

메시지 종류

설명

모든 서비스를 의미
auth
login과 같이 인증프로그램 유형이 발생한 메시지
authprive
개인 인증을 요하는 프로그램 유형이 발생한 메시지
cron
cron, at과 같은 프로그램이 발생한 메시지
daemon
telneted, ftpd과 같이 daemon이 발생한 메시지
kern
커널이 발생한 메시지
lpr
프린트 유형의 프로그래이 발생한 메시지
mail
mail 시스템이 발생한 메시지
mark
syslogd에 의해 만들어지는 날짜 유형
news
유즈넷 뉴스 프로그램 유형이 발생한 메시지
syslog
syslog 프로그램이 유형이 발생한 메시지
user
사용자 프로세스
uucp
UUCP 시스템이 발생한 메시지
local0 ~ local7
여분으로 남겨둔 유형
※ facility 뒤에 .none을 붙이면 해당 facility를 제외하곘다는 의미 (mail.none은 메일 관련 메시지를 제외한다는 뜻이다.)

③ 메시지 우선 순위(priority)

- 위험의 정도를 가리키며 설정된 위험의 정도보다 높아야 메시지를 내보낸다.
- 레벨 앞에 '='을 사용할 경우 해당 레벨의 위험도와 같은 경우를 의미
- priority의 종류 (위험 레벨이 낮은 것부터 높은 순서로 나열)

우선 순위
설명

발생하는 모든 상황에 대한 메시지
debug
프로그램을 디버깅할 때 발생하는 메시지
info
통계, 기본정보 메시지
notice
특별한 주의를 요하나 에러는 아닌 메시지
warning
주의를 요하는 경고 메시지
err
에러가 발생하는 경우의 메시지
crit
크게 급하지는 않지만 시스템에 문제가 생기는 단계의 메시지
alert
즉각적인 조정을 해야 하는 상황
emerg
모든 사용자들에게 전달되어야 할 위험한 상황
none
어떠한 경우라도 메시지를 저장하지 않음
④ action 종류

종류
설명
file
해당 file에 내용을 추가

@host
지정된 호스트로 메시지를 보냄

user
지정된 사용자의 스크린으로 메시지를 보냄
현재 로그인되어 있는 모든 사용자의 스크린으로 메시지를 보냄

# vim /etc/syslog.conf 파일

1. 모든 info메시지를 기록하되, mail, news, authpriv, cron은 제외 한다.
2. 개인인증관련은 /var/log/secure에 기록 한다.
3. 모든 메일관련 메시지는 /var/log/maillog에 기록 한다.
4. cron관련 메시지는 /var/log/cron에 기록 한다.
5. 모든 emerg이상의 에러가 발생하면 모든 사용자에게 알려준다.
6. uucp, news의 crit 정보기록은 /var/log/spooler에 기록 한다.
7. 부트 메시지는 /var/log/boot.log에 기록 한다.

8. Log File의 종류

- 기본적인 로그들은 syslogd에 의해서 제어가 되며, syslogd의 설정파일인 /etc/syslog.conf 파일을 수정함으로써 이 파일들의 저장위치와 저장파일명을 변경 가능하다.
- 보안을 위하여 숨김속성(.으로 시작하는 디렉토리)의 디렉토리를 다른곳에 만들어 숨김속성파일(.으로 시작하는 파일)을 만들어서 찾기 힘든 곳에 보관 할 수 있다.

로그이름
로그 파일명
관련 데몬
설명
커널 로그
/dev/console
kernel
콘솔에 뿌려지는 로그
시스템 로그
/var/log/messages
syslogd
리눅스 커널로그 및 주된 로그
보안 로그
/var/log/secure
xinetd
보안 인증 관련 로그
메일 로그
/var/log/maillog
sendmail popper
메일 로그
(sendmail에 의한 로그)
크론 로그
/var/log/cron
crond
crond에 의한 로그
부팅 로그
/var/log/boot.log
kernel
시스템 부팅시의 로그
커널 부트 메시지 로그
/var/dmesg
kernel
부팅될 당시의 각종 메시지들 저장
커널 로그
/var/log/wtmp
kernel
시스템 전체 로그인 기록 저장
커널 로그
/var/log/utmp
kernel
현재 로그인 사용자에 대한 기록, 사용자 ip 저장
FTP 로그
/var/log/xferlog
ftpd
ftp 로그
웹 로그
/var/log/httpd/access_log
httpd
아파치(웹서버) 로그 저장
웹 로그
/var/log/httpd/error_log
httpd
아파치(웹서버) 에러 저장
네임서버 로그 /var/log/named.log named 네임서버(DNS) 로그

4. Log File 분석

① 콘솔 로그 (/dev/console)

- 커널(kernel)에 관련된 내용을 시스템콘솔에 뿌려주는 로그 이다.
- messages 내용과 일치하지는 않지만 시스템에 관련된 중요한 내용들(시스템풀, 다운 등)에 대한 로그를 관리자에게 알리고자 함이 목적이다.
- 출력을 파일로 저장하는 것이 아니라 장치명(/dev/console)을 사용하여 콘솔로 로그를 뿌려준다.
- timestamp, 호스트명, 커널 메시지 내용 등이 기록 되었다.

② 시스템 로그 (/var/log/messages) - 주로 접속 시 인증에 관한 것과 메일에 관한 내용, 시스템에 관한 변경사항 등 시스템에 관한 전반적인 로그를 기록하는 파일 이다. - timestamp, 호스트명, 데몬명, 메시지 내용 등이 기록 된다. - 시스템 관리자에 의해서 가장 소중하게 다루어지는 로그 이다.
(보안사고가 발생시에 가장 먼저 분석을 해야하는 파일이다.) - 메시지 내용은 su 실패에 대한 로그, 특정 데몬이 비활성화된 로그, 부팅 시 발생된 에러 등 다양한 로그들을 포함한다. - syslog facility에 의하여 남은 로그로 /etc/syslog.conf에서 어떻게 설정이 되어 있느냐에 따라 남는 정보의 종류가 달라진다. - 사용명령어 : dmesg (/var/log/messages를 출력한다.)

# tail -f /var/log/messages

# dmesg

# vim /var/log/messages

③ 보안 로그 (/var/log/secure) - 모든 접속과 관련하여 언제 어디서 어떤 서비스를 사용했는지 기록 한다. - timestamp, 호스트명, 응용프로그램명[pid], 메시지 내용이 기록되어 있다. - 보통 login, tcp_wrappers, xinetd 관련 로그들이 남는다. - ps -ef라는 옵션 외에도 aux라는 옵션으로 확인 가능하다.
( 예 : ps aux | grep xinetd ) - 실행중인 xinetd의 PID저장 파일은 /var/run/xinetd.pid

# tail -f /var/log/secure

# ps aux | grep xinetd

# vim /var/log/secure

④ 메일 로그 (/var/log/maillog)

- sendmail이나 pop등의 실행에 관한 기록 이다.
- 메일을 주고받을 때에 이 로그파일에 기록(smtp와 pop에 관한 로그)
- 실행중인 sendmail의 PID저장 파일은 /var/run/sendmail.pid
- timestamp, 호스트명, 데몬명[pid], 메시지 내용 기록

# tail -f /var/log/maillog

# vim /var/log/maillog

⑤ 크론 로그 (/var/log/cron)

- 시스템의 정기적인 작업에 대한 모든 작업한 기록을 보관하고 있는 파일이다.
  (crond에 의해서 생성되는 로그가 기록되는 파일)
- 크론데몬의 crond가 언제 어떤작업을 했는가를 확인 가능히다.
- crond의 의해서 실행되었던 데몬(프로세스, 응용프로그램 등)들이 기록 되었다.
- 실행중인 crond의 PID저장 파일은 /var/run/crond.pid
- /etc/ 디릭토리 밑에 있는 cron.hourly, crondaily, cron.weekly, cron.monthly 파일들에 기록되어 있는 작업을 실행한 후에 cron 파일에 log를 기록한다.
- timestamp, 호스트명, 데몬명[pid], 메시지 내용이 기록되어 있다.

# tail -f /var/log/cron

# vim /var/log/cron

⑥ 부팅로그 (/var/log/boot.log)

- 시스템의 데몬들이 실행되거나 재시작되었을 때 기록되는 로그 파일이다.
- 부팅 시의 에러나 조치 사항을 확인할 때 활용이 가능하다.
- timestamp, 호스트명, 데몬명[pid], 메시지 내용이 기록 된다.

⑦ 커널 부트 메시지 로그 (/var/dmesg)

- 시스템이 부팅할 때 출력되었던 메시지를 로그 기록한다.
  ⑧ /var/log/wtmp
- 사용자들의 로그인-아웃 정보 기록
- 바이너리 형태이며 지금까지 사용자들의 로그인, 로그아웃 히스토리를 모두 누적형태로 저장된다.
- 시스템의 셧다운, 부팅 히스토리까지 포함한다. ( 해킹 피해 시스템 분석 시 중요)
- 사용 명령어 : last

옵션
설명
last [계정명]
계정명을 입력하면 사용자별 로그 정보를 출력한다.
last -f [파일명]
지난 파일에 대해서 로그를 점검시 -f 옵션 뒤에 해당 파일명을 입력
last -R
IP를 제외시킨 로그 정보를 출력한다.
last -a
로그 정보를 출력할 때 IP를 뒤로 배치해서 출력한다.
last -d
외부에서 접속한 정보와 reboot 정보만을 출력한다.

# last

⑨ /var/log/utmp

- 시스템에 현재 로그인한 사용자들에 대한 상태를 기록한다.
- /var/run(Linux) 혹은 /var/adm, /etc/(Solaris)등에 위치하며 바이너리 형태로 저장되어 vi 편집기 등으로 읽을 수 없다.
- utmp(x) 파일은 기본적으로 사용자 이름, 터미널 장치 이름, 원격 로그인 시 원격 호스트 이름, 사용자 로그인한 시간 등을 기록 한다.
- 사용자 명령어 : who, w, whodo, uesrs, finger
- "w"는 utmp(x)를 참조하여 현재 시스템에 성공적으로 로그인한 사용자에 대한 snapshot을 제공해 주는 명령으로 해킹 피해 시스템 분석 시에 반드시 실행해 보아야 하는 명령어이다.

# w

# who

# users

# finger

※ wtmp, wtmpx와 파일 포맷은 동일하나 ump(x)에는 현재 시스템에 대한 정보가 남고 wtmp(x)에는 누적된 정보가 남는다는 것이 가장 큰 차이점 이다.
⑩ /var/log/lastlog

- /etc/passwd 파일에 정의되어 있는 모든 계정의 최근 접속 정보를 확인 가능하다.
- 사용자의 최근 로그인 시간을 사용자 이름, 터미널, IP 주소, 마지막 로그인 시간 출력
- /var/log/lastlog 파일에 저장되고 바이너리 형태
- 사용 명령어 : lastlog

옵션
설명
-u / --login
접속 이름
-t / --time
날짜
(현재 시간부터 입력하나 날짜까지 접속자 검색)
-h / --help
도움말

# lastlog

⑪ FTP 로그 (/var/log/xferlog)

- ftp나 ncftp등의 접속이 이루어 졌을 때 이 로그파일에 기록이 된다.
- ftp를 사용했을 때 이 로그파일에 기록되고, 업로드 파일과 다운로드한 파일들에 대한 자세한 정보가 기록 저정된다.

# tail -f /var/log/xferlog

# cat xferlog | more

⑫ 웹 로그 (/var/log/httpd/access_log, /var/log/httpd/error_log)

▶ Access log - 웹사이트에 접속했던 사람들이 각 파일들을 요청했던 실적을 기록해놓은 목록을 저장한다. - 방문자의 IP또는 도메인 네임, 방문자가 파일을 요청한 시간, 방문자가 웹서버에 요청한 처리 내용(Get, Put, Head), 방문자가 요구한 파일의 이름, 파일의 크기 및 처리결과 등의 데이터를 제공한다.
▶ Error log - 요청한 홈페이지가 없거나 링크가 잘못되는 등의 오류가 있을 경우에 생성된다.

⑬ /var/log/btmp

- 로그인 시도 5번 이상 실패한 로그 기록을 확인 가능하다.
- 계정명, 접속 콘솔/터미널 유무, IP, 시간 정보 출력
- /var/log/btmp에 바이너리 형태로 저장도니다.
- 사용자 명령어 : lastb

# lastb

⑭ History (해당 계정의 home directory/ .bash_history)

- 접속한 계정에서 사용했던 명령어의 내용만 보여준다.
- root의 경우 ~/.bash_history에 사용한 명령어가 저장된다.
- 저장되는 로그의 위치를 변경하려면 export HISTFILE="경로/파일이름" 을 입력 한다.

# history

⑮ Pacct (/var/account/pacct)

- 시스템에 들어온 사용자가 어떤 명령어를 실행시키고 어떠한 작업을 했는지에 대한 사용 내역 등이 기록 된다.
- 사용된 명령어의 argument와 그 명령어가 시스템 내 어느 파일 시스템의 어느 디렉토리에 실행되었는지는 기록되지 않는다.
- /var/account/pacct에 바이너리 파일로 기록된다.
- 파일 크기가 쉽게 커지기 때문에 관리가 필요한 파일 이다.
- 사용자 명령어 : lastcomm / acctcom

1. Linux Log 관리

2)  logrotate 의미

- /var/log 디렉토리 안에 있는 많은 로그파일은 기존의 파일에 덧붙여지게 되므로 크기는 계속 커지게 된다.
- 이를 방지하기 위해서 로그 파일을 조각으로 나눌 수 있는데, 이런 작업을 하는 프로그램이 logrotate 이다.

3.  logrotate 특징

▶ 로그 자동 관리를 위한 로테이트 처리 - crond에 의해서 주기적으로 실행되는 logrotated 데몬에 의해 수행된다. - 로테이트(rotate) 작업내용은 로그파일 지르기(rotate), 보관, 삭제, 압축, 메일로 보내기 등 - 해당 조건체크의 실행은 crond에 의해 주기적으로 자동 실행되지만, 로테이트 작업이 발생하기 위해서는 해당 조건에 해당되어야 한다. - /etc/logrotate.conf파일과 /etc/logrotate.d/ 디렉토리 내에 있는 파일들에서 해당 조건 설정한다.

▶ 로테이트(rotate) 처리 - 해당 날짜 또는 용량 이상이 되었을 때 로그파일을 로테이트(size) - 로테이트 작업 직전과 직후에 특정작업을 수행 가능하다.
(prerotate/endscript, postrotate/endscript) - 로테이트 작업을 하면서 압축 / 비압축이 가능하다. (compress, nocompress) - 로테이트 후에 보관할 파일의 수를 지정 가능하다.(rotate) - 로테이트 후에 생성되는 파일의 소유주와 퍼미션 등을 설정 가능하다. (create) - 로테이트 후에 생성되는 파일의 확장자 임의로 지정 가능하다. (extension)

# vim /etc/logrotate.conf

1. weekly : 로그파일에 대해서는 일주일(weekly) 마다 rotate
2. rotate 4 : 최대 4번까지 rotate를 허용 한다.
   (logfile, logfile.1 ~ logfile.4까지의 로그파일이 생성)
3. create : rotate한 후에 비어있는 로그파일을 생성
4. compress : 로그파일을 압축하는 옵션 이다. (기본 값은 활성화되어 있지 않다.) 용량문제가 크게 되지 않는다면 압축을 하지 않는 것이 좋다.
5. include /etc/logrotate.d ; 대부분 RPM패키지로 설치되는 데몬들은 이 디렉토리에 로그파일이 생성 된다.
   (로그파일을 rotate시킬 수 있도록 하는 설정이다.)

6. no packages won wtmp -- we'll rotate them here : 아래에 있는 로그파일(wtmp)은 어떤 패키지에 의해서도 설정되지 않기 때문에 아래에서 따로 설정한다. 다른 로그파일들은 /etc/logrotate.d 내의 파일들에서 모두 설정한다.
   /var/log/wtmp {
   monthly
   minsize 1M
   create 0664 root utmp
   rotate 1

}
한달마다 rotate 하며 최소 크기는 1M, 최대 1회까지만 그리고 rotate 관련파일인 utmp파일을 생성한다.

※ 리눅스 서버에서 logrotate은 /etc/cron.daily 디렉토리에 cron작업으로 등록되어 있어 매일이 실행되도록 설정되어 있다.

===================================================

보안기사 필수 Log 파일

===================================================

1. utmp

1) 현재 시스템에 로그인한 사용자의 로그인 정보 저장.
2) 형식 : 바이너리 형식
3) 확인 : who, w, finger (명령어)
4) 경로 : /var/run/utmp : find / | grep utmp (확인)

2. wtmp

1) 전체 사용자의 로그인 및 로그아웃 정보를 저장.
2) 형식 : 바이너리 형식
3) 확인 : last (명령어)
4) 경로 : /var/log/wtmp : find / | grep wtmp (확인)

3. secure

1) 텔넷이나 SSH 등의 원격 족속등에서 발생한 인증 정보를 로그로 저장
2) 형식 : 텍스트
3) 확인 : 파일 편집기(vi, vim), cat, tail(실시간 확인 : -f)
4) 특정파일 검색 방법 cat secure.1 | grep ftp

4. lastlog

1) 각 사용자의 최근 로그인 시간, 사용자 이름, 터미널, 마지막 로그인 시간 등이 로그로 저장
2) 형식 : 바이너리 형식
3) 확인 : lastlog
4) 경로 : /var/log/lastlog

5. btmp (= faillog)

1) 5회 이상 실패한 로그인 시도 정보를 로그로 저장
2) 형식 : 바이너리 형식
3) 확인 : lastb
4) 경로 : /usr/bin/lastb

6. messages

1) 리눅스 시스템의 로그인 기록, 디바이스 정보, 시스템 설정오류, 파일 시스템, 네트워크 세션 기록 등 전반적인 시스템 동작내용이 기록되는 로그 파일

※ iptables -L : 방화벽 정책
※ 메일 로그

7. sulog (su가 사용한 모든 흔적들을 저장)

   1. su 명령 사용 내역이 기록되는 로그파일

[출처] [Linux Log File] 리눅스 로그파일 종류 및 분석|작성자 kdi0373

### reference

[리눅스 로그파일 종료 및 분석](https://blog.naver.com/kdi0373/220522832069)
