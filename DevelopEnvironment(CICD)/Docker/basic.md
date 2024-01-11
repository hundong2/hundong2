# docker study page

## Window WSL Docker run ( not for windows )

```sh
@echo Starting dockerd in WSL ...
@echo off
for /f "tokens=1" %%a in ('wsl sh -c "hostname -I"') do set wsl_ip=%%a
        netsh interface portproxy add v4tov4 listenport=2375 connectport=2375 connectaddress=%wsl_ip%
        wsl -d Ubuntu -u root -e nohup sh -c "dockerd -H tcp://%wsl_ip% &" < nul > nul 2>&1
```

or

### docker3.bat

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

## docker images

```sh
REPOSITORY           TAG                IMAGE ID       CREATED         SIZE
dotnetdocker         latest             37611f461d61   44 hours ago    3.08GB
```

## docker image run

```sh
docker run --name [NAMES: docker ps -a] -v [local mount path]:[docker mount path] -it
```

```sh
docker run --name dotnetdocker -v /mnt/d/workspace:/mnt -it dotnetdocker:latest [REPOSITORY: docker images]:[TAG: docker images]
```

## docker ps list

```sh
docker ps -a

CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                    PORTS     NAMES
a1174a276ecb   4de4ec5bf9e0   "/bin/bash"              47 hours ago   Up 41 hours                         dotnetdocker3
28cbe2d9946f   4de4ec5bf9e0   "/bin/bash"              47 hours ago   Exited (1) 47 hours ago             dotnetdocker2
```

## docker run

```sh
docker run --name [NAMES: docker ps] -v [local mount path]:[docker mount path] -it [REPOSITORY: docker images]:[TAG: docker images]
```

```sh
docker run --name dotnetdocker -v /mnt/d/workspace:/mnt -it dotnetdocker:latest
```

## docker container start ( or docker exec command )

```sh
docker start [Container ID: docker ps]
```

```sh
docker start a1174a276ecb
```

## docker exec

```sh
docker exec -it [Container ID: docker ps] /bin/bash
```

```sh
docker exec -it a1174a276ecb /bin/bash
```

## docker commit

```sh
docker commit -m "initialize git" [Container ID: docker ps] [REPOSITORY: docker images]:[TAG: docker images]
```

```sh
docker commit -m "initialize git" a1174a276ecb dotnetdocker:latest
```

## docker images

### docker image save

```sh
docker save [option] <compress filename> [REPOSITORY:TAG]
```

```sh
docker save -o dotnetbuild.tar dotnetdocker:latest
or
docker save dotnetdocker:latest | gzip > dotnetbuild.tar.gz
```

### docker load

```sh
docker load -i <compressed filename>
```

```sh
docker load -i dotnetbuild.tar
```

### docker import

```sh
docker import <file name or URL> [REPOSITORY:TAG]
```

## information

-i : interactive
-t : tty(로그)
/bin/bash : Use /bin/bash

## fingerprint error ssh

```sh
sudo sed -i s/"#   StrictHostKeyChecking ask"/"   StrictHostKeyChecking no"/g /etc/ssh/ssh_config
cat /etc/ssh/ssh_config | grep StrictHostKeyChecking
```

or

```sh
sudo sed -i 's/#\?StrictHostKeyChecking\s\+ask/StrictHostKeyChecking no/g' /etc/ssh/ssh_config
```

## reference

### normal

- [Docker for powershell](https://velog.io/@klasis/Windows%EC%97%90%EC%84%9C-CMDPowershell%EB%A1%9C-Docker%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%8B%A4%EB%A3%A8%EA%B8%B0)
- [Docker NDK Binary Execute](https://ganadist.github.io/2018_12_29_docker_qemu_user_arm.html)
- [Docker container SSL certificates](https://stackoverflow.com/questions/26028971/docker-container-ssl-certificates)
- [Docker Hub Dotnet SDK](https://hub.docker.com/_/microsoft-dotnet-sdk/)
- [Docker Image push](https://nicewoong.github.io/development/2018/03/06/docker-commit-container/)

### dotnet docker

- [Dotnet Docker Sample - Github](https://github.com/dotnet/dotnet-docker/blob/main/samples/dotnetapp/README.md)
- [Docker File - Github](https://github.com/dotnet/dotnet-docker/blob/main/samples/dotnetapp/Dockerfile)
- [Dotnet Deps Docker hub](https://hub.docker.com/r/ubuntu/dotnet-deps)

### erorr debugging

- [[Docker] Error response from daemon: Get "https://registry-1.docker.io/v2/": x509: certificate signed by unknown authority](https://velog.io/@ptah0414/Docker-Error-response-from-daemon-Get-httpsregistry-1.docker.iov2-x509-certificate-signed-by-unknown-authority-%EC%97%90%EB%9F%AC)
- [Unknown authority signs certificate for Docker pull](https://copyprogramming.com/howto/docker-pull-certificate-signed-by-unknown-authority)
- ["docker pull" certificate signed by unknown authority](https://stackoverflow.com/questions/50768317/docker-pull-certificate-signed-by-unknown-authority)
- [System has not been booted with systemd as init system (PID 1). Can't operate](https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate)
- [Failed to verify certificate: x509: certificate signed by unknown authority](https://github.com/docker/genai-stack/issues/84)
- [Unable to connect to the server: x509: certificate signed by unknown authority - zetawiki](https://zetawiki.com/wiki/Unable_to_connect_to_the_server:_x509:_certificate_signed_by_unknown_authority)
- [In wsl Ubuntu I can't copy the SSL certificate into the docker container - stackoverflow](https://stackoverflow.com/questions/77431590/in-wsl-ubuntu-i-cant-copy-the-ssl-certificate-into-the-docker-container)
