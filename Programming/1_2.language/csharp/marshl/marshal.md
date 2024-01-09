# Marshal with C++

## 1. Marshal whit shared memory data 

### 1.1 IntPtr to Memory Struct Data 

- c# struct and c++ struct connect
```c#
public struct MemoryData
{
    ...;
}
```

```c++
struct MemoryData
{
    ...;
}
```

- Marshal using
- c# side 
- dll library use from clr library

#### code from c# 
```c# 
IntPtr mPtrdata; //sharedmemory data pointer
MemoryData mData = new MemoryData[{MemoryData struct size}];
mData = Marshal.PtrToStructure<MemoryData>(mPtrdata);
```
#### reference information 
[PtrToStructure](https://docs.microsoft.com/ko-kr/dotnet/api/system.runtime.interopservices.marshal.ptrtostructure?view=net-6.0#system-runtime-interopservices-marshal-ptrtostructure-1(system-intptr))  
[c#, c++ sharedmemory](https://kaylab.tistory.com/9)  
[c++ image transfer to c#](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=roboinside&logNo=221178543629)  
[IntPtr Using C#](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=nimi315&logNo=50101013158)  
[Marshal struct input](http://www.todayhumor.co.kr/board/view.php?table=programmer&no=5257)  
[IntPtr structure from microsoft](https://docs.microsoft.com/ko-kr/dotnet/api/system.intptr?view=net-6.0)  



