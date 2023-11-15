# .NET Environment

## 1. .NET7

## 1.1 install

### 1.1.1 use script

- [Ubuntu에 .NET SDK 또는 .NET 런타임 설치](https://learn.microsoft.com/ko-kr/dotnet/core/install/linux-ubuntu)
- [설치 스크립트를 사용하거나 이진 파일을 추출하여 Linux .NET 설치](https://learn.microsoft.com/ko-kr/dotnet/core/install/linux-scripted-manual#scripted-install)
- [.NET Install scripts](https://dotnet.microsoft.com/en-us/download/dotnet/scripts)
- [.NET Install guide](https://learn.microsoft.com/ko-kr/dotnet/core/tools/dotnet-install-script?WT.mc_id=dotnet-35129-website)

#### dotnet-install.sh 사용법

```sh
dotnet-install.sh  [--architecture <ARCHITECTURE>] [--azure-feed]
    [--channel <CHANNEL>] [--dry-run] [--feed-credential]
    [--install-dir <DIRECTORY>] [--jsonfile <JSONFILE>]
    [--no-cdn] [--no-path] [--quality <QUALITY>]
    [--runtime <RUNTIME>] [--runtime-id <RID>]
    [--skip-non-versioned-files] [--uncached-feed] [--keep-zip] [--zip-path <PATH>] [--verbose]
    [--version <VERSION>]

dotnet-install.sh --help
```

```sh
# Get Ubuntu version
declare repo_version=$(if command -v lsb_release &> /dev/null; then lsb_release -r -s; else grep -oP '(?<=^VERSION_ID=).+' /etc/os-release | tr -d '"'; fi)

# Download Microsoft signing key and repository
wget https://packages.microsoft.com/config/ubuntu/$repo_version/packages-microsoft-prod.deb -O packages-microsoft-prod.deb

# Install Microsoft signing key and repository
sudo dpkg -i packages-microsoft-prod.deb

# Clean up
rm packages-microsoft-prod.deb

# Update packages
sudo apt update
```

### 1.1.2 Download gz file

- [dotnet script build](https://dotnet.microsoft.com/ko-kr/download/dotnet/thank-you/sdk-7.0.403-linux-x64-binaries)

```sh
mkdir -p $HOME/dotnet && tar zxf dotnet-sdk-7.0.403-linux-x64.tar.gz -C $HOME/dotnet
export DOTNET_ROOT=$HOME/dotnet
export PATH=$PATH:$HOME/dotnet
```

### 1.1.3 Use apt get

- [microsoft user guide](https://learn.microsoft.com/ko-kr/dotnet/core/install/linux-ubuntu)

```sh
sudo apt update
sudo apt upgrade dotnet-sdk-7.0
```

### 1.1.4 Install instructions for Linux ( github )

[dotnet-core-github](https://github.com/dotnet/core/blob/main/release-notes/7.0/install-linux.md)

### 1.1.5 dotnet install download dotnet.tar.gz << - it is used

```sh
curl -Lo dotnet.tar.gz https://download.visualstudio.microsoft.com/download/pr/f5c74056-330b-452b-915e-d98fda75024e/18076ca3b89cd362162bbd0cbf9b2ca5/dotnet-sdk-7.0.100-rc.2.22477.23-linux-x64.tar.gz
mkdir dotnet
tar -C dotnet -xf dotnet.tar.gz
rm dotnet.tar.gz
export DOTNET_ROOT=~/dotnet
export PATH=$PATH:~/dotnet
dotnet --version
```

## 1.2 Build

- Platform build
  - linux
    ```sh
    build foldername(project) --os linux -a x64 -o foldername/bin/Debug/net7.0-linux-x64
    ```
  - osx
    ```sh
    build foldername(project) --os osx -a x64 -o foldername/bin/Debug/net7.0-osx-x64
    ```
  - window
    ```sh
    build foldername(project) --os win -a x64 -o foldername/bin/Debug/net7.0-win-x64
    ```

## reference

[.NET7 SDK Download site - linux](https://dotnet.microsoft.com/ko-kr/download/dotnet/thank-you/sdk-7.0.403-linux-x64-binaries)  
[Ubuntu에 .NET SDK or .NET runtime 설치](https://learn.microsoft.com/ko-kr/dotnet/core/install/linux-ubuntu)  
[C# 콘솔 앱 템플릿은 최상위 문을 생성합니다.](https://learn.microsoft.com/ko-kr/dotnet/core/tutorials/top-level-templates)  
[Framework 대상 지정 개요](https://learn.microsoft.com/ko-kr/visualstudio/ide/visual-studio-multi-targeting-overview?view=vs-2022)
[.NET Build User Guide](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build)

## dotnet build error tip

- [curl: (60) SSL certificate problem: self signed certificate in certificate chain](../23.error/curl_error.md) << - it is used
- [Unable to load the service index for source https://api.nuget.org/v3/index.json](../23.error/nuget_error.md)
- ["NU1301: Failed to retrieve information about 'Microsoft.NETCore.App.Host.win-x64' from remote source 'https://api.nuget.org/v3-flatcontainer/microsoft.netcore.app.host.win-x64/index.json'."](../23.error/nuget_error.md)
-

### libicu-dev 설치

```sh
sudo apt-get -y install libicu-dev
```

[libicu-dev install message](https://installati.one/install-libicu-dev-ubuntu-20-04/)
[dotnet build](https://learn.microsoft.com/ko-kr/dotnet/core/tutorials/with-visual-studio-code?pivots=dotnet-7-0)
