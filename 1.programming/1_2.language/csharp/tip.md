# C# tip information 

## 1. clr

### 1.1 clr error 

```
Fatal error: "No Target Architecture" in Visual Studio
```
- u can use to write document(c#) top 

```c#
#define WIN32_LEAN_AND_MEAN      // Exclude rarely-used stuff from Windows headers
#include <windows.h>
```

#### reference 
[stackoverflow](https://stackoverflow.com/questions/4845198/fatal-error-no-target-architecture-in-visual-studio)  
[c++ dll using](https://cypsw.tistory.com/entry/C-C-DLL-%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)  
[clr library using](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jackylim&logNo=100119927187)  

## 2. Managed & Unmanaged 

### reference 

[c# 자원관리](https://gammabeta.tistory.com/1538)  


## 3. Programming conception 

[English version](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/)  
[Korean version](https://docs.microsoft.com/ko-kr/dotnet/csharp/programming-guide/concepts/)  


## 3. static new 

- 상속받은 자식노드에서 function을 재정의 할때 헷갈리지 않게 하기 위한 작업. 

```csharp
class Foo
{
    public static void Do() { Console.WriteLine("Foo.Do"); }
}
class Bar : Foo // :Foo added
{
    public static void Something()
    {
        Do();
    }
    public static new void Do() { Console.WriteLine("Bar.Do"); }
}
```
[stackoverflow](https://stackoverflow.com/questions/661246/what-is-the-point-of-static-new-modifier-for-a-function)  

## 4. C# PublishSingleFile Option

### reference 

[C# - PublishSingleFile과 관련된 옵션](https://www.sysnet.pe.kr/2/0/13159?pageno=0)  

