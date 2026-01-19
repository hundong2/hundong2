# VSCode Deep Dive Guide

이 가이드는 VSCode의 설정 파일과 다양한 개발 환경에서의 디버그 설정을 상세히 설명합니다. 이 문서를 통해 개발 환경 설정에 소비하는 시간을 최소화할 수 있습니다.

## 목차
1. [기초 지식](#기초-지식)
2. [VSCode settings.json 설명](#vscode-settingsjson-설명)
3. [다양한 개발 환경에서의 Debug 설정](#다양한-개발-환경에서의-debug-설정)
4. [settings.json에서 사용 가능한 글로벌 환경변수](#settingsjson에서-사용-가능한-글로벌-환경변수)

---

## 기초 지식

### VSCode 설정 파일의 종류

VSCode는 주로 3가지 JSON 설정 파일을 사용합니다:

```
프로젝트 루트/
├── .vscode/
│   ├── settings.json      # 워크스페이스별 설정
│   ├── launch.json        # 디버그 구성
│   └── tasks.json         # 작업 자동화 구성
```

- **settings.json**: 편집기 설정, 확장 프로그램 설정, 언어별 설정
- **launch.json**: 디버그 및 실행 구성
- **tasks.json**: 빌드, 테스트 등의 작업 자동화

### JSON 기본 구조

```json
{
  "key": "value",
  "arrayKey": ["item1", "item2"],
  "objectKey": {
    "nestedKey": "nestedValue"
  }
}
```

**주의사항:**
- 마지막 항목 뒤에는 쉼표(`,`)를 붙이지 않습니다
- 문자열은 큰따옴표(`"`)로 감싸야 합니다
- 주석은 `//` 또는 `/* */`로 작성 가능 (JSON with Comments)

### VSCode 확장 설치 방법

1. **UI를 통한 설치:**
   - `Ctrl+Shift+X` (Windows/Linux) 또는 `Cmd+Shift+X` (Mac)
   - 확장 마켓플레이스에서 검색 후 설치

2. **명령 팔레트를 통한 설치:**
   - `Ctrl+Shift+P` (Windows/Linux) 또는 `Cmd+Shift+P` (Mac)
   - "Extensions: Install Extensions" 입력

---

## VSCode settings.json 설명

### settings.json 위치

VSCode는 두 가지 레벨의 설정을 지원합니다:

```
User Settings (전역 설정)
├── Windows: %APPDATA%\Code\User\settings.json
├── macOS: ~/Library/Application Support/Code/User/settings.json
└── Linux: ~/.config/Code/User/settings.json

Workspace Settings (프로젝트별 설정)
└── 프로젝트루트/.vscode/settings.json
```

### User Settings vs Workspace Settings

| 구분 | User Settings | Workspace Settings |
|------|--------------|-------------------|
| 범위 | 모든 프로젝트에 적용 | 해당 워크스페이스만 적용 |
| 우선순위 | 낮음 | 높음 (User Settings 덮어쓰기) |
| 공유 | Git에 포함되지 않음 | Git에 포함 가능 |
| 용도 | 개인 선호 설정 | 팀 공통 설정 |

**설정 우선순위 흐름:**
```
Default Settings → User Settings → Workspace Settings → 최종 적용
```

### 실제 폴더 구조 예제

```
my-project/
├── .vscode/
│   ├── settings.json          # 프로젝트별 설정
│   ├── launch.json            # 디버그 설정
│   └── tasks.json             # 작업 설정
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── pyproject.toml
└── README.md
```

### settings.json 예제

#### 기본 편집기 설정

```json
{
  // 편집기 기본 설정
  "editor.fontSize": 14,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.rulers": [80, 120],
  
  // 파일 설정
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "files.encoding": "utf8",
  "files.trimTrailingWhitespace": true,
  
  // 터미널 설정
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.shell.linux": "/bin/bash"
}
```

#### 언어별 설정

```json
{
  // Python 전용 설정
  "[python]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  
  // JavaScript/TypeScript 전용 설정
  "[javascript]": {
    "editor.tabSize": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.tabSize": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  
  // C# 전용 설정
  "[csharp]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": true
  }
}
```

#### Python 개발 설정 예제

```json
{
  // Python 인터프리터 설정
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  
  // Linting 설정
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": ["--max-line-length=120"],
  
  // Formatting 설정
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length=120"],
  
  // Testing 설정
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "python.testing.unittestEnabled": false,
  
  // Type checking
  "python.analysis.typeCheckingMode": "basic"
}
```

#### .NET 개발 설정 예제

```json
{
  // OmniSharp 설정 (C# 언어 서버)
  "omnisharp.enableRoslynAnalyzers": true,
  "omnisharp.enableEditorConfigSupport": true,
  "omnisharp.enableImportCompletion": true,
  
  // C# 포매팅
  "csharp.format.enable": true,
  "csharp.suppressDotnetInstallWarning": false,
  
  // .NET Core 디버거
  "dotnet.defaultSolution": "${workspaceFolder}/MyProject.sln"
}
```

---

## 다양한 개발 환경에서의 Debug 설정

### launch.json 기본 구조

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "설정 이름",
      "type": "디버거 타입",
      "request": "launch 또는 attach",
      "program": "실행할 프로그램",
      // 기타 설정들...
    }
  ]
}
```

**주요 필드:**
- `name`: 디버그 구성 이름 (디버그 패널에 표시)
- `type`: 디버거 종류 (`python`, `coreclr`, `node` 등)
- `request`: `launch` (새로 실행) 또는 `attach` (실행 중인 프로세스에 연결)
- `program`: 실행할 프로그램 경로

### Python UV 환경에서의 현재 열려있는 파일 디버그 방법

#### 환경 준비

1. **UV 설치 및 프로젝트 설정:**

```bash
# UV 설치
curl -LsSf https://astral.sh/uv/install.sh | sh

# 프로젝트 초기화
uv init my-project
cd my-project

# 가상환경 생성
uv venv

# 패키지 설치
uv pip install requests numpy pandas
```

2. **필요한 VSCode 확장:**
   - Python (ms-python.python)
   - Pylance (ms-python.vscode-pylance)

#### 폴더 구조

```
my-python-project/
├── .venv/                    # UV로 생성된 가상환경
│   ├── bin/
│   │   └── python
│   └── lib/
├── .vscode/
│   ├── settings.json         # Python 인터프리터 설정
│   └── launch.json           # 디버그 구성
├── src/
│   ├── main.py
│   ├── module1.py
│   └── utils/
│       └── helper.py
├── tests/
│   └── test_main.py
├── pyproject.toml
└── uv.lock
```

#### .vscode/settings.json 설정

```json
{
  // UV 가상환경의 Python 인터프리터 지정
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  
  // Python 경로 설정
  "python.envFile": "${workspaceFolder}/.env",
  
  // 자동 활성화
  "python.terminal.activateEnvironment": true,
  
  // Pylance 설정
  "python.analysis.extraPaths": [
    "${workspaceFolder}/src"
  ],
  "python.analysis.typeCheckingMode": "basic"
}
```

#### .vscode/launch.json 설정

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: 현재 파일 디버그",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true,
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src"
      }
    },
    {
      "name": "Python: 현재 파일 디버그 (인자 포함)",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "args": [
        "--input", "data.txt",
        "--output", "result.txt"
      ],
      "justMyCode": true
    },
    {
      "name": "Python: 모듈로 실행",
      "type": "python",
      "request": "launch",
      "module": "src.main",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: 현재 파일 디버그 (외부 라이브러리 포함)",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": false,
      "stopOnEntry": false
    },
    {
      "name": "Python: Django 디버그",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": [
        "runserver",
        "0.0.0.0:8000"
      ],
      "django": true,
      "justMyCode": true
    },
    {
      "name": "Python: FastAPI 디버그",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "src.main:app",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8000"
      ],
      "jinja": true,
      "justMyCode": true
    },
    {
      "name": "Python: Pytest 현재 파일",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": [
        "${file}",
        "-v",
        "-s"
      ],
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

#### 디버그 실행 방법

1. **브레이크포인트 설정:**
   - 코드 줄 번호 왼쪽 클릭하여 빨간 점 추가

2. **디버그 시작:**
   - `F5` 키 누르기
   - 또는 `Run and Debug` 패널 (Ctrl+Shift+D) > 원하는 구성 선택 > 재생 버튼 클릭

3. **디버그 컨트롤:**
   - `F5`: Continue (계속 실행)
   - `F10`: Step Over (다음 줄로)
   - `F11`: Step Into (함수 안으로)
   - `Shift+F11`: Step Out (함수 밖으로)
   - `Ctrl+Shift+F5`: Restart
   - `Shift+F5`: Stop

#### Python 예제 코드

**src/main.py:**
```python
import sys
from pathlib import Path

def calculate_sum(numbers: list[int]) -> int:
    """숫자 리스트의 합계를 계산합니다."""
    total = 0
    for num in numbers:
        total += num  # 여기에 브레이크포인트 설정
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    print(f"합계: {result}")
    
    # 명령줄 인자 처리
    if len(sys.argv) > 1:
        print(f"받은 인자: {sys.argv[1:]}")

if __name__ == "__main__":
    main()
```

### .NET 환경에서의 CSX 파일 또는 프로젝트 디버그 방법

#### 환경 준비

1. **.NET SDK 설치:**

```bash
# Ubuntu/Debian
wget https://dot.net/v1/dotnet-install.sh
chmod +x dotnet-install.sh
./dotnet-install.sh --channel 8.0

# Windows (PowerShell)
winget install Microsoft.DotNet.SDK.8

# macOS
brew install --cask dotnet-sdk
```

2. **필요한 VSCode 확장:**
   - C# (ms-dotnettools.csharp)
   - C# Dev Kit (ms-dotnettools.csdevkit) - 선택사항

3. **프로젝트 생성:**

```bash
# 콘솔 앱 생성
dotnet new console -n MyConsoleApp
cd MyConsoleApp

# 웹 API 생성
dotnet new webapi -n MyWebApi
```

#### .NET 프로젝트 폴더 구조

```
MyDotNetProject/
├── .vscode/
│   ├── launch.json           # 디버그 구성
│   ├── tasks.json            # 빌드 작업 구성
│   └── settings.json
├── src/
│   ├── MyConsoleApp/
│   │   ├── Program.cs
│   │   ├── MyConsoleApp.csproj
│   │   └── appsettings.json
│   └── MyLibrary/
│       ├── Calculator.cs
│       └── MyLibrary.csproj
├── tests/
│   └── MyConsoleApp.Tests/
│       ├── ProgramTests.cs
│       └── MyConsoleApp.Tests.csproj
├── scripts/
│   ├── example.csx           # C# 스크립트 파일
│   └── utils.csx
└── MyDotNetProject.sln
```

#### .vscode/launch.json 설정 (프로젝트)

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": ".NET Core: 현재 프로젝트 디버그",
      "type": "coreclr",
      "request": "launch",
      "preLaunchTask": "build",
      "program": "${workspaceFolder}/src/MyConsoleApp/bin/Debug/net8.0/MyConsoleApp.dll",
      "args": [],
      "cwd": "${workspaceFolder}/src/MyConsoleApp",
      "console": "internalConsole",
      "stopAtEntry": false
    },
    {
      "name": ".NET Core: 웹 API 디버그",
      "type": "coreclr",
      "request": "launch",
      "preLaunchTask": "build",
      "program": "${workspaceFolder}/src/MyWebApi/bin/Debug/net8.0/MyWebApi.dll",
      "args": [],
      "cwd": "${workspaceFolder}/src/MyWebApi",
      "stopAtEntry": false,
      "serverReadyAction": {
        "action": "openExternally",
        "pattern": "\\bNow listening on:\\s+(https?://\\S+)"
      },
      "env": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      },
      "sourceFileMap": {
        "/Views": "${workspaceFolder}/Views"
      }
    },
    {
      "name": ".NET Core: Attach to Process",
      "type": "coreclr",
      "request": "attach",
      "processId": "${command:pickProcess}"
    }
  ]
}
```

#### .vscode/tasks.json 설정

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build",
      "command": "dotnet",
      "type": "process",
      "args": [
        "build",
        "${workspaceFolder}/src/MyConsoleApp/MyConsoleApp.csproj",
        "/property:GenerateFullPaths=true",
        "/consoleloggerparameters:NoSummary"
      ],
      "problemMatcher": "$msCompile",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "publish",
      "command": "dotnet",
      "type": "process",
      "args": [
        "publish",
        "${workspaceFolder}/src/MyConsoleApp/MyConsoleApp.csproj",
        "/property:GenerateFullPaths=true",
        "/consoleloggerparameters:NoSummary"
      ],
      "problemMatcher": "$msCompile"
    },
    {
      "label": "watch",
      "command": "dotnet",
      "type": "process",
      "args": [
        "watch",
        "run",
        "--project",
        "${workspaceFolder}/src/MyConsoleApp/MyConsoleApp.csproj"
      ],
      "problemMatcher": "$msCompile"
    },
    {
      "label": "clean",
      "command": "dotnet",
      "type": "process",
      "args": [
        "clean",
        "${workspaceFolder}/src/MyConsoleApp/MyConsoleApp.csproj"
      ],
      "problemMatcher": "$msCompile"
    }
  ]
}
```

#### CSX (C# 스크립트) 파일 디버그 설정

CSX 파일은 C# 스크립트 파일로, dotnet-script를 사용하여 실행합니다.

1. **dotnet-script 설치:**

```bash
dotnet tool install -g dotnet-script
```

2. **.vscode/launch.json에 CSX 디버그 구성 추가:**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "C#: 현재 CSX 스크립트 실행",
      "type": "coreclr",
      "request": "launch",
      "program": "dotnet",
      "args": [
        "script",
        "${file}"
      ],
      "cwd": "${workspaceFolder}",
      "console": "internalConsole",
      "stopAtEntry": false,
      "internalConsoleOptions": "openOnSessionStart"
    },
    {
      "name": "C#: 현재 CSX 스크립트 디버그 (인자 포함)",
      "type": "coreclr",
      "request": "launch",
      "program": "dotnet",
      "args": [
        "script",
        "${file}",
        "--",
        "arg1",
        "arg2"
      ],
      "cwd": "${fileDirname}",
      "console": "internalConsole",
      "stopAtEntry": false
    },
    {
      "name": "C#: CSX 스크립트 디버그 (고급)",
      "type": "coreclr",
      "request": "launch",
      "program": "${env:HOME}/.dotnet/tools/dotnet-script",
      "args": [
        "${file}",
        "-d"
      ],
      "cwd": "${fileDirname}",
      "console": "internalConsole",
      "stopAtEntry": false,
      "logging": {
        "moduleLoad": false
      }
    }
  ]
}
```

#### CSX 예제 코드

**scripts/example.csx:**
```csharp
#!/usr/bin/env dotnet-script

using System;
using System.Linq;
using System.Collections.Generic;

// 간단한 계산 함수
int Calculate(int a, int b)
{
    var result = a + b;  // 여기에 브레이크포인트 설정
    Console.WriteLine($"{a} + {b} = {result}");
    return result;
}

// 명령줄 인자 처리
var args = Args.ToArray();
Console.WriteLine($"받은 인자 개수: {args.Length}");

if (args.Length >= 2 && int.TryParse(args[0], out int num1) && int.TryParse(args[1], out int num2))
{
    Calculate(num1, num2);
}
else
{
    // 기본값으로 실행
    Calculate(10, 20);
}

// 리스트 처리 예제
var numbers = new List<int> { 1, 2, 3, 4, 5 };
var sum = numbers.Sum();
Console.WriteLine($"합계: {sum}");
```

#### .NET 프로젝트 예제 코드

**src/MyConsoleApp/Program.cs:**
```csharp
using System;
using System.Threading.Tasks;

namespace MyConsoleApp
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("프로그램 시작");
            
            // 브레이크포인트 설정 예제
            var calculator = new Calculator();
            var result = calculator.Add(10, 20);
            
            Console.WriteLine($"결과: {result}");
            
            // 비동기 메서드 호출
            await ProcessDataAsync();
            
            Console.WriteLine("프로그램 종료");
        }
        
        static async Task ProcessDataAsync()
        {
            Console.WriteLine("비동기 작업 시작");
            await Task.Delay(1000);  // 1초 대기
            Console.WriteLine("비동기 작업 완료");
        }
    }
    
    public class Calculator
    {
        public int Add(int a, int b)
        {
            return a + b;  // 브레이크포인트 설정 가능
        }
        
        public int Multiply(int a, int b)
        {
            return a * b;
        }
    }
}
```

#### 디버그 실행 흐름도

```
[파일 열기]
    │
    ▼
┌─────────────┐
│파일 타입 확인│
└─────┬───────┘
      │
      ├──── .py ────► [Python 디버그 구성 선택]
      │                      │
      ├──── .cs ────► [.NET 디버그 구성 선택]
      │         .csproj       │
      │                      │
      └──── .csx ────► [CSX 디버그 구성 선택]
                            │
                            ▼
                  [브레이크포인트 설정]
                            │
                            ▼
                     [F5로 디버그 시작]
                            │
                            ▼
                  [preLaunchTask 실행]
                    (빌드 등)
                            │
                            ▼
                     [디버거 연결]
                            │
                            ▼
              [브레이크포인트에서 정지]
                            │
                            ▼
              [변수 검사 / 스택 추적]
                            │
                            ▼
                    ┌───────┴───────┐
                    │   계속 실행?   │
                    └───┬───────┬───┘
                        │       │
            F5: Continue│       │F10/F11: Step
                        │       │
                        └───┬───┘
                            │
                      [반복 또는 종료]
```

---

## settings.json에서 사용 가능한 글로벌 환경변수

VSCode는 설정 파일에서 사용할 수 있는 여러 사전 정의된 변수를 제공합니다.

### 주요 환경변수 목록

| 변수 | 설명 | 예제 |
|------|------|------|
| `${workspaceFolder}` | 현재 워크스페이스의 루트 폴더 경로 | `/home/user/my-project` |
| `${workspaceFolderBasename}` | 워크스페이스 폴더 이름 | `my-project` |
| `${file}` | 현재 열린 파일의 절대 경로 | `/home/user/my-project/src/main.py` |
| `${fileBasename}` | 현재 열린 파일의 이름 | `main.py` |
| `${fileBasenameNoExtension}` | 확장자를 제외한 파일 이름 | `main` |
| `${fileExtname}` | 현재 파일의 확장자 | `.py` |
| `${fileDirname}` | 현재 열린 파일이 있는 디렉터리 경로 | `/home/user/my-project/src` |
| `${fileDirnameBasename}` | 파일이 있는 디렉터리 이름 | `src` |
| `${relativeFile}` | 워크스페이스 기준 상대 경로 | `src/main.py` |
| `${relativeFileDirname}` | 워크스페이스 기준 디렉터리 상대 경로 | `src` |
| `${cwd}` | 현재 작업 디렉터리 | `/home/user/my-project` |
| `${lineNumber}` | 커서가 있는 줄 번호 | `42` |
| `${selectedText}` | 선택된 텍스트 | `def main():` |
| `${execPath}` | VSCode 실행 파일 경로 | `/usr/share/code/code` |
| `${pathSeparator}` | OS별 경로 구분자 | `/` (Linux/Mac), `\` (Windows) |
| `${env:NAME}` | 환경변수 값 | `${env:HOME}` → `/home/user` |
| `${config:NAME}` | 다른 설정값 참조 | `${config:python.pythonPath}` |
| `${command:NAME}` | 커맨드 실행 결과 | `${command:python.interpreterPath}` |

### 환경변수 사용 예제

#### 예제 1: Python 프로젝트의 경로 설정

```json
{
  // 가상환경 경로
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  
  // 테스트 디렉터리
  "python.testing.pytestArgs": [
    "${workspaceFolder}/tests"
  ],
  
  // 추가 Python 경로
  "python.analysis.extraPaths": [
    "${workspaceFolder}/src",
    "${workspaceFolder}/lib"
  ],
  
  // 환경변수 파일
  "python.envFile": "${workspaceFolder}/.env"
}
```

#### 예제 2: 다중 워크스페이스 프로젝트

```
multi-workspace/
├── frontend/
│   ├── .vscode/
│   │   └── settings.json
│   └── src/
├── backend/
│   ├── .vscode/
│   │   └── settings.json
│   └── src/
└── workspace.code-workspace
```

**workspace.code-workspace:**
```json
{
  "folders": [
    {
      "path": "frontend",
      "name": "Frontend"
    },
    {
      "path": "backend",
      "name": "Backend"
    }
  ],
  "settings": {
    "files.exclude": {
      "**/node_modules": true,
      "**/.venv": true
    }
  }
}
```

#### 예제 3: 환경변수를 활용한 launch.json

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: 현재 파일",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "cwd": "${fileDirname}",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src:${workspaceFolder}/lib",
        "APP_ENV": "development",
        "LOG_LEVEL": "DEBUG"
      }
    },
    {
      "name": ".NET: 프로젝트 실행",
      "type": "coreclr",
      "request": "launch",
      "program": "${workspaceFolder}/bin/Debug/net8.0/${workspaceFolderBasename}.dll",
      "args": [],
      "cwd": "${workspaceFolder}",
      "env": {
        "ASPNETCORE_ENVIRONMENT": "Development",
        "CONNECTION_STRING": "${env:DB_CONNECTION_STRING}"
      }
    }
  ]
}
```

#### 예제 4: tasks.json에서 환경변수 활용

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "빌드",
      "type": "shell",
      "command": "python",
      "args": [
        "${workspaceFolder}/build.py",
        "--output",
        "${workspaceFolder}/dist/${fileBasenameNoExtension}"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": []
    },
    {
      "label": "현재 파일 실행",
      "type": "shell",
      "command": "python ${file}",
      "options": {
        "cwd": "${fileDirname}",
        "env": {
          "PYTHONPATH": "${workspaceFolder}/src"
        }
      }
    },
    {
      "label": ".NET 빌드",
      "type": "process",
      "command": "dotnet",
      "args": [
        "build",
        "${workspaceFolder}/${fileBasenameNoExtension}.csproj"
      ],
      "group": "build"
    }
  ]
}
```

#### 예제 5: 조건부 설정 (플랫폼별)

```json
{
  "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
  "terminal.integrated.shell.linux": "/bin/bash",
  "terminal.integrated.shell.osx": "/bin/zsh",
  
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  
  // Windows 전용 설정
  "python.defaultInterpreterPath.windows": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  
  // 환경변수 사용
  "terminal.integrated.env.linux": {
    "PATH": "${env:HOME}/.local/bin:${env:PATH}",
    "WORKSPACE": "${workspaceFolder}"
  },
  "terminal.integrated.env.windows": {
    "PATH": "${env:USERPROFILE}\\.local\\bin;${env:PATH}",
    "WORKSPACE": "${workspaceFolder}"
  }
}
```

### 커맨드 변수 활용

VSCode 명령어를 변수로 사용할 수 있습니다.

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: 인터프리터 선택",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      // 실행 시 Python 인터프리터 선택 대화상자 표시
      "python": "${command:python.interpreterPath}"
    },
    {
      "name": "사용자 입력 받기",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "args": [
        // 실행 시 사용자에게 입력 요청
        "${input:userInput}"
      ]
    }
  ],
  "inputs": [
    {
      "id": "userInput",
      "type": "promptString",
      "description": "프로그램에 전달할 인자를 입력하세요",
      "default": "default_value"
    },
    {
      "id": "pickEnvironment",
      "type": "pickString",
      "description": "환경을 선택하세요",
      "options": [
        "development",
        "staging",
        "production"
      ],
      "default": "development"
    }
  ]
}
```

### 환경변수 디버깅 팁

실제 변수 값을 확인하려면:

1. **터미널에서 확인:**
```bash
# Linux/Mac
echo ${workspaceFolder}

# Windows (PowerShell)
echo $env:workspaceFolder
```

2. **launch.json에 로깅 추가:**
```json
{
  "configurations": [
    {
      "name": "Debug with logging",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "logging": {
        "engineLogging": true
      }
    }
  ]
}
```

3. **디버그 콘솔에서 확인:**
   - 디버그 실행 후 Debug Console에서 환경변수 확인 가능

---

## 추가 팁과 베스트 프랙티스

### 1. 팀 공유 설정 관리

**.vscode/settings.json (팀 공유):**
```json
{
  // 모든 팀원이 사용할 설정
  "editor.formatOnSave": true,
  "editor.tabSize": 4,
  "python.linting.enabled": true,
  "python.testing.pytestEnabled": true
}
```

**개인 User Settings (공유하지 않음):**
```json
{
  // 개인 취향 설정
  "editor.fontSize": 14,
  "workbench.colorTheme": "Dark+ (default dark)",
  "terminal.integrated.shell.linux": "/bin/zsh"
}
```

### 2. .gitignore에 개인 설정 제외

```gitignore
# 개인 설정은 커밋하지 않음
.vscode/settings.json

# 팀 공유 설정은 커밋
!.vscode/launch.json
!.vscode/tasks.json
```

### 3. 설정 계층 구조

```
[Default Settings]
      │
      ▼
[User Settings]
      │
      ▼
[Workspace Settings]
      │
      ▼
[Folder Settings]
      │
      ▼
[최종 적용 설정]
```

**우선순위:** Folder Settings > Workspace Settings > User Settings > Default Settings

### 4. 추천 확장 프로그램 설정

**.vscode/extensions.json:**
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-dotnettools.csharp",
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "eamodio.gitlens"
  ],
  "unwantedRecommendations": [
    "ms-vscode.csharp"
  ]
}
```

### 5. 스니펫(Snippet) 활용

**User Snippets (Python):**
```json
{
  "Python Main": {
    "prefix": "pymain",
    "body": [
      "def main():",
      "    ${1:pass}",
      "",
      "",
      "if __name__ == '__main__':",
      "    main()"
    ],
    "description": "Create main function"
  }
}
```

### 6. 원격 개발 (Remote Development)

SSH, Container, WSL 환경에서도 동일한 설정 사용:

```json
{
  // 원격 환경 설정
  "remote.SSH.defaultExtensions": [
    "ms-python.python"
  ],
  "remote.containers.defaultExtensions": [
    "ms-python.python",
    "ms-dotnettools.csharp"
  ]
}
```

### 7. 자주 사용하는 단축키

| 단축키 | 기능 |
|--------|------|
| `Ctrl+Shift+P` | 명령 팔레트 |
| `Ctrl+P` | 파일 빠른 열기 |
| `Ctrl+Shift+D` | 디버그 패널 |
| `F5` | 디버그 시작 |
| `Ctrl+F5` | 디버그 없이 실행 |
| `F9` | 브레이크포인트 토글 |
| `F10` | Step Over |
| `F11` | Step Into |
| `Ctrl+\`` | 터미널 토글 |
| `Ctrl+B` | 사이드바 토글 |

---

## 문제 해결 (Troubleshooting)

### Python 디버거가 시작되지 않는 경우

1. **Python 확장 설치 확인:**
   ```bash
   code --list-extensions | grep python
   ```

2. **Python 인터프리터 경로 확인:**
   - `Ctrl+Shift+P` > "Python: Select Interpreter"
   - 올바른 가상환경 선택

3. **launch.json 검증:**
   ```json
   {
     "name": "Python: Current File",
     "type": "python",  // 정확한 타입 확인
     "request": "launch",
     "program": "${file}",
     "console": "integratedTerminal"
   }
   ```

### .NET 디버거가 작동하지 않는 경우

1. **OmniSharp 로그 확인:**
   - `Ctrl+Shift+P` > "OmniSharp: Show OmniSharp Log"

2. **C# 확장 재설치:**
   ```bash
   code --uninstall-extension ms-dotnettools.csharp
   code --install-extension ms-dotnettools.csharp
   ```

3. **빌드 작업 확인:**
   ```bash
   dotnet build
   ```

### 환경변수가 인식되지 않는 경우

1. **변수 문법 확인:**
   - 올바른 형식: `${workspaceFolder}`
   - 잘못된 형식: `$workspaceFolder` 또는 `{workspaceFolder}`

2. **경로 구분자 확인:**
   - Windows: `\\` 또는 `/` (둘 다 가능)
   - Linux/Mac: `/`

3. **.env 파일 로드 확인:**
   ```json
   {
     "python.envFile": "${workspaceFolder}/.env"
   }
   ```

---

## 참고 자료

- [VSCode 공식 문서](https://code.visualstudio.com/docs)
- [VSCode Debugging 가이드](https://code.visualstudio.com/docs/editor/debugging)
- [VSCode Variables Reference](https://code.visualstudio.com/docs/editor/variables-reference)
- [Python in VSCode](https://code.visualstudio.com/docs/python/python-tutorial)
- [.NET in VSCode](https://code.visualstudio.com/docs/languages/csharp)
- [UV 공식 문서](https://github.com/astral-sh/uv)
- [dotnet-script GitHub](https://github.com/filipw/dotnet-script)

---

## 마치며

이 가이드를 통해 VSCode의 설정과 디버그 환경을 효율적으로 구성할 수 있습니다. 핵심 포인트:

1. **settings.json**: User vs Workspace 설정 구분
2. **launch.json**: 언어별 디버그 구성 이해
3. **환경변수**: `${workspaceFolder}` 등 활용
4. **팀 협업**: .vscode 폴더를 Git으로 공유

질문이나 추가 사항이 있다면 이슈를 생성해 주세요!
