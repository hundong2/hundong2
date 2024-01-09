# fetal error 

## 1. C1189 ( winnt.h 사용 시 )

```bash
No Target Architecture
```

- "Windows.h"헤더 파일을 우선적으로 include ( 맨 위에 선언 ) 

## 2. MSB3073 ( VCEnd Error )

- project 경로( 파일 ) 띄어쓰기 있을경우 발생. 

- 프로젝트 - 속성 - 구성 속성 - 빌드 이벤트 - 빌드 후 이벤트 - 명령줄을 수정

변경전  

```
copy $(ProjectDir)Text.txt $(OutputPath)
```

변경후  

```
copy "$(ProjectDir)Text.txt" "$(OutputPath)"
```