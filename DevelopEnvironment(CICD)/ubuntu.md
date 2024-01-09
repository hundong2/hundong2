# ubuntu

## APT INSTALL

### MSBUILD

[msbuild opensource](https://github.com/dotnet/msbuild/blob/main/documentation/wiki/Building-Testing-and-Debugging-on-.Net-Core-MSBuild.md)

### Apt-Get Update Failing because of Certificate Validation

[Apt-Get Update Failing because of Certificate Validation](https://serverfault.com/questions/1093511/apt-get-update-failing-because-of-certificate-validation)  
[apt-get update server certificate verification failed](https://github.com/Azure/azure-cli/issues/19405)  
[ubuntu 20.04 apt source repository](https://jkim83.tistory.com/102)  
[apt-get update failed because certificate verification failed because handshake failed on nodesource](https://askubuntu.com/questions/1095266/apt-get-update-failed-because-certificate-verification-failed-because-handshake)

### docker ubuntu

[ubuntu docker](https://hub.docker.com/_/ubuntu)

### WSL Ubuntu

[WSL - Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?](https://forums.docker.com/t/wsl-cannot-connect-to-the-docker-daemon-at-unix-var-run-docker-sock-is-the-docker-daemon-running/116245)  
[Cannot connect to the Docker daemon at unix:/var/run/docker.sock. Is the docker daemon running?](https://stackoverflow.com/questions/44678725/cannot-connect-to-the-docker-daemon-at-unix-var-run-docker-sock-is-the-docker)  
[Linux systemctl 명령 에러 System has not been booted with systemd as init system (PID 1).](https://parkkingcar.tistory.com/96)  
[[WSL] 윈도우 하위 리눅스 재부팅, 재시작 방법](https://webisfree.com/2022-11-08/[WSL]-%EC%9C%88%EB%8F%84%EC%9A%B0-%ED%95%98%EC%9C%84-%EB%A6%AC%EB%88%85%EC%8A%A4-%EC%9E%AC%EB%B6%80%ED%8C%85-%EC%9E%AC%EC%8B%9C%EC%9E%91-%EB%B0%A9%EB%B2%95)

### How To Install libicu-dev on Ubuntu 20.04

[How To Install libicu-dev on Ubuntu 20.04](https://installati.one/install-libicu-dev-ubuntu-20-04/)

```sh
sudo apt-get update
sudo apt-get -y install libicu-dev
```

## c++ update

```bash
apt-get update
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110 --slave /usr/bin/g++ g++ /usr/bin/g++-11
```

## dpkg package

### package list

```sh
dpkg --list
dpkg --list | grep [program name]
```

### package purge ( delete package )

```sh
dpkg --purge [program name]
```

## sudo: python command not found

- [stack overflow - sudo: python: command not found](https://stackoverflow.com/questions/44726377/sudo-python-command-not-found)

## environment setting

- There should be no spaces on the left or right of =.

### command setting

```sh
export [name]=[value]
```

```sh
env | grep [name]
```

### bashrc modify

```sh
vim /etc/bash.bashrc
or
vi ~/.bashrc
```

and

```sh
source /etc/bash.bashrc
or
source ~/.bashrc
```

### Clear environment variables

```sh
unset [environment variable name]
```
