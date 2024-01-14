# [C++] __stdcall, __cdecl 그리고 Calling Convention
  
함수호출 방식이 __cdecl, __pascal, __stdcall로 여러 가지가 있는 이유는 윈도우즈의 역사성에 있다. 우선 win16에서는 실행파일의 크기가 줄어들고 속도가 빠르다는 이유로 pascall 방식을 사용 했고 win32에서는 가변매개인자를 지원하는 함수를 제외한 모든 함수들은 __stdcall을 사용 한다. 만약 c 방식의 함수호출을 원한다면 __cdecl을 명시해 주어야 한다.(윈도우즈 프로그래밍에 있어서) 우선 c 방식의 함수 호출과 pascal 방식의 함수호출의 차이점을 알아보자. 첫 번째로 함수호출후 종료 시점에 호출한 함수의 스택을 정리하는 주체가 호출한 함수이냐 아니면 호출당한 함수이냐의 차이이다. 두 번째는 매개인자를 스택에 넣는 방향에 따라 나눈다. 즉, 다음과 같이 정리할 수가 있다.  
(언더바는 생략가능함 )  
1.인수를 스택에 집어넣는 방향에 따라서 다음과 같이 나뉘고  
       pascal : 인수를 스택에 저장하는 순서를 왼쪽에서 오른쪽으로 한다.  
       cdecl : 인수를 스택에 저장하는 순서를 오른쪽에서 왼쪽으로 한다.  
      stdcall : 인수를 스택에 저장하는 순서를 오른쪽에서 왼쪽으로 한다.  
2.스택에 인수를 pop 하는 주체에 따라서 다음과 같이 나뉘고.  
      pascal : 호출을 당하는 쪽이 스택공간을 삭제한다.  
      stdcall : 호출을 당하는 쪽이 스택공간을 삭제한다.  
     cdecl : 호출을 하는 쪽이 스택공간을 삭제한다.   
이렇게 stdcall은 pascal방식과 cdecl방식을 혼합한 형태를 띄운다 
자 이제는 WinMain함수를 살펴보자 일반적으로 WinMain은 다음과 같이 선언되어 있다.  
int APIENTRY WinMain( HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR pCmdLine, int nCmdShow )  
APIENTRY는 WINAPI와 같은 형식을 나타낸다. 이것은 FAR __stdcall로 정의되어 있다. 또한 참고로 CALLBACK은 __stdcall로 정의되어 있다. 그럼 WINAPI와 __cdecl 함수의 호출 방식의 차이점을 예제로 알아보도록 하자. 아래에 두 방식으로 호출되는 간단한 예제가 있다.  
```
#include "stdafx.h"
int __stdcall func(int i,int j);
int __cdecl func2(int i,int j);

int _tmain(int argc, _TCHAR* argv[])
{
        func(1,2);
        func2(2,3);
        return 0;
}
int __stdcall func(int i,int j)
{
        int r;
        r=i+j;
        return r;
}
int __cdecl func2(int i,int j)
{
        int r;
        r=i+j;
        return r;
}

```

이 함수들을 호출하는 부분을 디스어셈블 해 보갰다.  

```
        func(1,2);
00411A1E  push        2    
00411A20  push        1    
00411A22  call        func (411069h) 
        func2(2,3);
00411A27  push        3    
00411A29  push        2    
00411A2B  call        func2 (4110FFh) 
00411A30  add         esp,8 <-------------- cdecl의 함수호출의 경우는 이 부분이 추가됨
        return 0;
...
...
00411AA0  ret         8    <------- func가 종료될 때 
...
00411AE0  ret              <--------func2가 종료될때
...
```
  

위에 보면은 func를 호출할 때는 없는 코드가 func2에는 있는 것을 볼 수가 있다. 바로 스택을 정리 해주는 코드이다. add         esp,8 이라는 것이다. 모든 함수 호출 형식이 이와 같았다면.. 실행 화일 코드에 add         esp,8라는 명령어가 더 들어가게 된다. 따라서 이 코드가 존재하지 않는 pascall 방식이 실행크기가 작아지게 된 것이다. 파스칼 호출 방식은 속도도 저 명령어 하나 만큼 빨라지게 되는 것이다. 여기에는 8086 아키텍쳐에 관련된 명령어가 그 원인으로 등장한다. 그리고 스택을 정리한다는 것 자체가 그 함수를 호출한 뒤에 add         esp,8으로 스택포인터를 인자의 크기만큼 변경을 시킨다는 이야긴데...근데 여기서 프로시저 즉 함수를 다 수행했을때 원래 상태로 돌아가게 될 때 쓰이는 명령어는 ret이다. 함수 시작하고, 함수가 끝났을때 ret 명령어로 호출한 부분으로 넘어가게 된다. 다시 말하면 이 명령어는 실행되던 함수를 바로 빠져나가게 된다. 따라서.. 스택을 정리할 시간이 전혀 없다. 이에 8086설계자들은 함수에서 리턴이 될 때 스택포인터(SP)를 적절한 위치로 리셋을 시킬 수 있는 ret명령어를 새로 제공을 하여 이 문제를 아주 손쉽게 해결해 버렸다. 즉 ret, n 이라는 명령어를 제공했다는 셈이다..   
어차피 리턴할 걸 스택 포인터가 정리되는 부분으로 아예 리턴을 해버리란 이야기다.. 이것은 가만히 앉아서 프로그램의 속도와 크기를 이점을 살리는 것이다. 
add         esp,8   ; -->> 추가된 코드..   
호출하는 부분에서 이렇게 코딩하는 대신 호출 받는부분에서 리턴할때 ret, 8으로 해결했다는 것이다.   
이래서 속도가 더빨라지는 것이다. 크기도 줄어들고..... 생각을 한번 해보자..... 이런식의 함수가 굉장히 많이 호출된다면..  크기나 실행 시간이 증가되는건 당연하지 않겠는가 ? 이 이유로 속도와 크기가 아주 중요시 되던 시절에(windows 3.0, 3.1이 널리 사용되던 시절에) OS/2와 Windows설계자들은 API함수를 설계할때 프로그램이 느려지고 크기가 커지는 C방식을 사용하지 않고 pascal이나 fortran이 사용하고 있는 방식으로 스택 프레임을 설계 하게 되었다. 바로 이런 이유가 바로 pascal방식에 비교해서 바로 cdecl의 단점이 되는 것이다. 자 이번에는 다시 위의 cdecl 호출의 장점을 보게 되면.. 가변매개인자를 사용할 수가 있다는 것인데... 즉, 매개인자를 오른쪽에서 왼쪽으로 집어 넣는 것이 왜 중요한가? 이다.
이것은 인자의 첫번째가 어디인지 확실하다는 것이다. 즉 알려진 장소에서 첫번째 인자를 찾아낼 수 있다는 장점으로 가변인자를 허용할 수 있다. 호출이 되었을대 스택의 맨 상위부분이 인자의 첫번째임은 확실하니까.... 이것이 cdecl방식의 장점이 되는 것이다. 함수호출이 끝난후 스택을 정리할 때 호출한쪽에서는 정확하게 Stack을 사용한 사이즈를 알고있기 때문에 문제가되지 않지만 호출당한쪽에서는 또다른 정보를 가지고 사용한 Stack의 사이즈를 알아야 하기 때문에 심각한 문제가 발생할수 있다는 것이다. 그러기 때문에 stdcall은 함수호출 방식은 파스칼을 따르고 있지만 가변매개인자는 지원하지 못하는 것이다. 가변매개인자를 꼭 사용해야만 한다면 반드시 cdecl을 사용해야만 한다.  


출처: https://mindgear.tistory.com/73 [정리:티스토리]