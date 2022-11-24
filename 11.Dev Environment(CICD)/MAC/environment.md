# MAC OS Development environment setting


- [MAC OS Development environment setting](#mac-os-development-environment-setting)
  - [1. homebrew](#1-homebrew)
    - [1.1 homebrew install](#11-homebrew-install)
    - [1.2 homebrew uninstall](#12-homebrew-uninstall)
    - [2. boost install ( c++ install )](#2-boost-install--c-install-)
  - [2. Machine learning environment](#2-machine-learning-environment)
    - [2.1 python](#21-python)
  - [3. VSCODE KOREAN 깨짐 현상](#3-vscode-korean-깨짐-현상)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



## 1. homebrew

### 1.1 homebrew install

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 1.2 homebrew uninstall

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
```

```bash
brew update
```

### 2. boost install ( c++ install )

```bash
brew install boost 
```

- installed path : /opt/homebrew/Celler/boost

## 2. Machine learning environment 

### 2.1 python

```bash
brew install python3 # python3 install 
pip3 install pandas
pip3 install numpy
pip3 install graphviz # not to do 
brew install graphviz # graphviz
```

## 3. VSCODE KOREAN 깨짐 현상

```
command + shift + p 
or
fn + F1
```

- "Configure Display Language" 에 KR 추가 ( install )
- restart

