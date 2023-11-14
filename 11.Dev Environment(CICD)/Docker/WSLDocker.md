# docker for WSL

[출처 - 넷마블 엔지니어링](https://netmarble.engineering/docker-on-wsl2-without-docker-desktop/)

[Docker is Updating and Extending Our Product Subscriptions](https://www.docker.com/blog/updating-product-subscriptions/)

    - WSL을 사용하여 Windows에 Linux 설치: https://learn.microsoft.com/ko-kr/windows/wsl/install
    - 가볍게 쓰려했던 WSL2가 무겁게 다가온 순간: https://netmarble.engineering/journey-to-wsl2-and-trouble-shooting/

WSL2 설치와 세팅을 마쳤다면, 이제 도커 엔진을 설치할 차례입니다.

## WSL2에 도커 엔진 설치

아래 가이드는 WSL 커널 버전 5.10을 기준으로 작성했습니다. WSL 커널 버전이 5.15 이상일 때는 새로 작성한 글을 참고하셔도 됩니다. 이 글과 새 글은 systemd를 지원하는 WSL 커널 버전 5.15의 특징을 살린 환경 설정 몇가지를 제외하면, 기본 맥락이 거의 동일합니다.  
– [잠깐 20초만 한눈을 팔면, 멈춰 서는 WSL](https://netmarble.engineering/wsl-status-changed-to-stopped-after-closing-terminal/)

WSL2에 특정 버전 도커를 지정해서 설치해야 하는 특별한 목적이 있지 않다면, 도커가 공식으로 제공하는 설치 스크립트를 이용하는 것이 좋습니다.

```sh
$ curl -sSL get.docker.com | sh

# Executing docker install script, commit: 4f282167c425347a931ccfd95cc91fab041d414f

WSL DETECTED: We recommend using Docker Desktop for Windows.
Please get Docker Desktop from https://www.docker.com/products/docker-desktop

You may press Ctrl+C now to abort this script.
+ sleep 20
```

도커 설치 스크립트를 실행 후에 WSL 환경에서는 도커 데스크톱을 쓰기를 추천한다는 문구(WSL DETECTED: We recommend using Docker Desktop for Windows.)가 나옵니다. 특별히 다른 반응을 하지 않고 20초만 기다리면, 도커 설치를 시작합니다.  
도커가 잘 설치됐는지 확인해보겠습니다.

```sh
$ docker --version

Docker version 20.10.18, build b40c2f6
```

## 편의를 위한 sudo 권한 설정

‘docker’ 명령어 실행시 매번 ‘sudo’를 입력하지 않으려면, ‘sudoer’에서 ‘sudo’ 권한 유저 유무를 확인해야 합니다.  
먼저 ‘sudo’ 그룹에 사용자가 들어가 있는지 확인해보겠습니다.

```sh
$ grep -E ‘%sudo|%wheel’ /etc/group

sudo:x:27:iamgroot
```

만약 ‘sudo:x:27:[username]’과 비슷한 메시지가 출력되지 않는다면, ‘sudoer’ 그룹에 사용자를 추가해야 합니다.

```sh
sudo usermod -aG sudo $USER
```

다음으로, ‘sudo’ 명령어를 쓸 수 있는 조건에 그룹이 들어가 있는지 확인해야 합니다.

```sh
$ sudo grep -E '%sudo|%wheel' /etc/sudoers

%sudo	ALL=(ALL:ALL)	ALL
```

예시처럼 ‘%sudo ALL=(ALL:ALL) ALL’과 비슷한 메시지가 나오는지 확인 후, 사용자를 ‘docker’ 그룹에 추가합니다.

```sh
sudo usermod -aG docker $USER
```

## 도커 컨텍스트 설정

도커 데스크톱이 자동으로 잡아주는 설정 중에는 도커 컨텍스트(Docker Context)도 있습니다. 도커 컨텍스트에는 도커 빌드나 배포 등 사용 과정에서 필요한 정보를 품고 있기 때문에, 환경 변수 설정을 해야 정상 동작 합니다.  
‘.profile’이나 ‘.bashrc’에 도커 컨텍스트 환경 변수를 미리 넣어두면, WSL 콘솔에 로그인할 때 자동으로 환경 변수를 적용받습니다. 아래는 ‘.profile’ 파일에 도커 컨텍스트 환경 변수를 추가하는 예시입니다.

```sh
echo '' >> ~/.profile
echo '# set DOCKER_HOST for docker default context' >> ~/.profile
echo 'wsl_ip=$(ip addr show eth0 | grep -oP "(?<=inet\s)\d+(\.\d+){3}")' >> ~/.profile
echo 'export DOCKER_HOST=tcp://$wsl_ip:2375' >> ~/.profile
```

추가한 ‘.profile’ 환경 변수를 적용받으려면, WSL을 재실행해야 합니다.  
WSL 재실행 전에는 도커 데몬 소켓 에러가 나지만, WSL 재실행 후에는 도커 데몬 소켓 에러 없이 바로 실행됩니다.

## 우분투 22.04 이상일 땐

만약 우분투 버전이 22.04 이상이라면, ‘iptables’ 설정을 먼저 변경하고 나서 이후 과정을 따라가야 합니다. 우분투 22.04 버전부터  
‘iptables-nft’가 기본 설정으로 잡혀있어서, WSL에서 도커를 사용할 때 호환성 이슈가 발생합니다. ‘iptables-nft’ 대신 ‘iptables-legacy’를 사용해야 도커 데몬을 실행할 수 있습니다.  
우분투 20.04 이하 버전을 WSL에서 사용하시는 분들은 확인만 하고 그냥 넘어가셔도 됩니다.

- Failure to install and run Docker in WSL Ubuntu 22.04 (works in 20.04): “Cannot connect to the Docker daemon”:
- https://github.com/docker/for-linux/issues/1406

```sh
sudo update-alternatives --config iptables

There are 2 choices for the alternative iptables (providing /usr/sbin/iptables).

  Selection    Path                       Priority   Status
------------------------------------------------------------
* 0            /usr/sbin/iptables-nft      20        auto mode
  1            /usr/sbin/iptables-legacy   10        manual mode
  2            /usr/sbin/iptables-nft      20        manual mode

Press <enter> to keep the current choice[*], or type selection number: 1

update-alternatives: using /usr/sbin/iptables-legacy to provide /usr/sbin/iptables (iptables) in manual mode
```

‘iptables’ 설정 화면에서 ‘1’을 입력해 ‘iptables-legacy’를 선택하고, WSL을 재부팅 합니다. (WSL 재실행이 아닌, wsl --shutdown으로 실행하는 재부팅입니다.)

## 도커 데몬 실행

이제 도커 엔진 설치를 마쳤으니, 도커 데몬을 실행하겠습니다.  
WSL 환경이라는 특징에 따라, WSL 내부로 직접 들어가지 않아도 윈도우에서 직접 WSL 내부 명령어를 실행할 수 있습니다.  
도커 데몬(Docker Daemon, dockerd)은 백그라운드에서 도는 서비스이므로, 윈도우에서 직접 WSL 내부에 데몬을 띄울 간단한 배치 파일을 활용하면 편의성을 높일 수 있습니다.  
아래는 WSL IP를 도커 데몬과 연결하는 예시 배치 스크립트입니다. 윈도우 메모장 등 편한 편집기에서 간단히 ‘start-dockerd-in-wsl.bat’ 등 편한 이름으로 저장하고 실행하면 됩니다.  
배치 파일 자체는 dockerd를 백그라운로 실행하고 바로 종료됩니다. (배치 파일은 관리자 권한으로 실행해야 합니다.)

```sh
@echo Starting dockerd in WSL ...
@echo off
for /f "tokens=1" %%a in ('wsl sh -c "hostname -I"') do set wsl_ip=%%a
netsh interface portproxy add v4tov4 listenport=2375 connectport=2375 connectaddress=%wsl_ip%
wsl -d Ubuntu -u root -e nohup sh -c "dockerd -H tcp://%wsl_ip% &" < nul > nul 2>&1
```

## WSL 커널 버전이 5.15 이상이라면

이 글을 최초에 쓰던 시점에는 WSL 커널 버전이 5.10이었습니다.  
시간이 많이 흐른 지금은 윈도우 업데이트에 맞물려 WSL 커널 버전이 5.15 이상인 분들이 늘어나면서,  
기존 배치 파일에서 동작하지 않는 옵션이 생겼습니다. 만약 WSL 커널 버전이 5.15 이상이라면, 배치 파일을 아래처럼 바꿔서 쓰시면 됩니다.

```sh
@echo Starting dockerd in WSL ...
@echo off
if exist nohup.out del /f /q nohup.out
for /f "tokens=1" %%a in ('wsl sh -c "hostname -I"') do set wsl_ip=%%a
netsh interface portproxy add v4tov4 listenport=2375 connectport=2375 connectaddress=%wsl_ip%

wsl -d Ubuntu -u root -e sudo systemctl stop docker.socket
wsl -d Ubuntu -u root -e sudo systemctl stop docker.service
wsl -d Ubuntu -u root -e nohup sh -c "dockerd -H tcp://%wsl_ip% &"
```

## 배치 파일 실행

배치 파일은 실행하고 바로 종료되지만, dockerd가 프로세스로 돌기 위한 웜업 시간이 다소 필요하므로 10~30초가량 대기후에 WSL 안으로 들어가서 확인하면 도커 데몬 정상 동작을 확인할 수 있습니다.

```
./start-dockerd-in-wsl.bat
```

    - 도커 데몬 실행 배치 파일을 윈도우 시작 프로그램에 등록하거나 작업 스케줄러로 등록해두면, 윈도우 부팅에 맞춰 자동으로 도커 데몬이 실행될 수 있게 설정할 수 있습니다.
    - 윈도우11에서는 WSL 속 ‘/etc/wsl.conf’ 파일의 ‘[boot] command’를 사용하면 윈도우 부팅에 맞춰 자동으로 도커 데몬을 실행할 수 있습니다.

WSL에서 ‘.profile’이나 ‘.bash’에 자동 실행 코드를 추가해서 WSL 콘솔로 셸 로그인 시에 도커 데몬을 자동으로 실행하는 방법도 있습니다.  
아래는 ‘.profile’에 도커 데몬 자동 실행을 설정하는 예시 설정입니다. 아래 설정 내용도 WSL 커널 버전 영향을 받으므로 꼭 참고해서 트러블슈팅하시길 바랍니다.
