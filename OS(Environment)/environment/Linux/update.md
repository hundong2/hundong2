# Update Tip

# 01. GCC Update

## GCC Version check

```bash
gcc --version

gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

[GCC Spec을 확인](https://gcc.gnu.org/projects/cxx-status.html#cxx20)  

## GCC Update

```bash
$ sudo add-apt-repository ppa:ubuntu-toolchain-r/test
$ sudo apt-get update
$ sudo apt-get install gcc-11 g++-11
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110 --slave /usr/bin/g++ g++ /usr/bin/g++-11
update-alternatives: using /usr/bin/gcc-11 to provide /usr/bin/gcc (gcc) in auto mode
$ sudo update-alternatives --config gcc
```

# 02. Ubuntu Update 

[Ubuntu update tip](ubuntu_update.md)  


## reference site

[kukuta.tistory - [gcc] Ubuntu 20.04에서 최신 버전 gcc설치하기](https://kukuta.tistory.com/394)  

