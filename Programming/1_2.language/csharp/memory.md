# Memory management 

## **items**

- [1. Memory leack](#1-memory-leaks)  


***
## 1. Memory leaks

닷넷 응용 프로그램이, GC를 내장한 CLR의 동작으로 인해 "모든 메모리"가 자동으로 회수된다는 믿음을 가지신 분들이 종종 있는데요, 물론 Native 시절만큼 new/delete를 확실하게 해야 하는 필요성은 많이 줄었지만 그래도 코딩 방식에 따라 - 너무나 당연하게 메모리 누수가 발생한다는 것을 주의해야 합니다. 간간이 이에 대한 설명을 중복적으로 하게 되는데, 게다가 한 번도 이에 관한 글을 쓴 적이 없어 이참에 한번 정리해 보려고 합니다.

마침 좋은 글도 있으니, ^^

8 Ways You can Cause Memory Leaks in .NET
; https://michaelscodingspot.com/ways-to-cause-memory-leaks-in-dotnet/

이번에는 저 글을 '내 맘대로' 번역해 정리해 보겠습니다.




### 1. 잘못된 이벤트 핸들러 관리

.NET Framework 응용 프로그램의 메모리 누수에 대한 사례 중 빠지지 않고 등장하는, 실제로 현업에서 은근히 실수를 많이 하게 되는 문제입니다. 엄밀히, 이 문제의 주요 원인은 C#에서의 delegate/event가 추상화를 너무 잘하기 때문입니다. 예를 들어 다음의 코드를 보면,

```c#
using System;

class Program
{
    static void Main(string[] args)
    {
        UILayout layout = new UILayout();

        while (true)
        {
            for (int i = 0; i < 1000; i++)
            {
                UIElement uiElem = new UIElement();
                layout.LayoutChanged += UIElement.s_Layout_LayoutChanged;
            }
        }
    }
}

public class UILayout
{
    public event EventHandler LayoutChanged;
}

public class UIElement
{
    public static void s_Layout_LayoutChanged(object sender, EventArgs e)
    {
    }
}
```

얼핏 LayoutChanged에 대한 이벤트 구독은 uiElem의 메서드와만 연결한 것이기 때문에 메모리 누수와는 무관할 듯해도, 실상은 (event의 근간이 되는) EventHandler delegate의 내부 동작 방식에서 메모리 누수로 연결이 됩니다. "public event EventHandler LayoutChanged"의 EventHandler는 System.MulticastDelegate를 상속받은 타입으로서, 이는 내부적으로 이벤트 구독의 대상 메서드를 목록으로 보관하기 때문에 결과적으로 봤을 때 "layout.LayoutChanged += uiElem.Layout_LayoutChanged" 코드는 의미적으로 다음과 같은 구현과 유사하다고 보면 됩니다.

```c#
layout.LayoutChanged.Add(uiElem.Layout_LayoutChanged);

public class UILayout
{
    public event List<EventHandler> LayoutChanged;
}
```

따라서, 저 구독을 해지하지 않으면 목록의 수는 늘어나고 결국 그만큼의 메모리 누수가 발생하는 것입니다. 그런데, 이 문제는 instance 유형의 메서드를 구독했을 때 더 심각해집니다.

```c#
using System;

class Program
{
    static void Main(string[] args)
    {
        UILayout layout = new UILayout();

        while (true)
        {
            for (int i = 0; i < 1000; i++)
            {
                UIElement uiElem = new UIElement();
                layout.LayoutChanged += uiElem.Layout_LayoutChanged;
            }
        }
    }
}

public class UILayout
{
    public event EventHandler LayoutChanged;
}

public class UIElement
{
    public void Layout_LayoutChanged(object sender, EventArgs e)
    {
    }
}
```

인스턴스 메서드인 경우, 의미상으로 보면 다음과 같이 인스턴스까지 함께 보관하는 식으로 동작하므로,

```c#
layout.LayoutChanged.Add(new EventHandler(uiElem, uiElem.Layout_LayoutChanged));

public class UILayout
{
    public event List<EventHandler> LayoutChanged;
}
```

GC는 이제 새로 생성된 UIElement가 블록 범위 밖으로 벗어났는데도 불구하고, 이벤트가 연결된 UILayout 인스턴스가 살아있는 한 그것을 해제하지 못하게 됩니다. 이런 모든 문제를 해결하는 간단한 방법은, 이벤트를 구독했으면 꼭 해제하는 코드도 넣으면 됩니다.

```c#
while (true)
{
    for (int i = 0; i < 1000; i++)
    {
        UIElement uiElem = new UIElement();
        layout.LayoutChanged += uiElem.Layout_LayoutChanged;
        layout.LayoutChanged -= uiElem.Layout_LayoutChanged;
    }
}
```



### 2. 익명 메서드 내에서의 캡처 변수 사용

원문의 예제를 보면, 익명 메서드를 Queue 등의 자료 구조를 이용해 보관하고 있으므로 어차피 그 Queue의 항목을 없애지 않으면 메모리 누수이기 때문에 캡처 변수가 꼭 메모리 누수라고 볼 수는 없습니다. (이런 면에서 봤을 때 event 구독 역시 "+=" 연산자를 이용한다는 측면에서 계속 누적된다는 의미를 지니므로 메모리 누수임을 짐작케 하는 면이 있습니다.)

하지만, 변수를 캡처하는 내부 동작에는 해당 변수를 소유한 인스턴스를 함께 보관하는 C# 컴파일러의 도움이 있다는 사실을 다시 한번 인지시킨다는 점에서 좋은 예제이니 읽어보실 것을 권장합니다.




### 3. 정적 변수의 사용

GC는 현재 참조가 유지되고 있는 객체들은 제거를 하지 못합니다. 다음의 그림을 보면,

gcroot_1.jpg

가장 하단에서의 참조로 인해 "Reachable Objects"들을 힙에서 제거할 수 없게 되는데, 이런 GC Root에는 다음과 같은 것들이 있습니다.

현재 실행 중인 스레드의 호출 스택
정적 변수
COM Interop 시 전달된 관리 개체의 인스턴스, ...

여기서 문제는 개발자가 정의할 수 있는 "정적 변수"인데요, 이 정적 변수가 참조하는 모든 하위 객체들은 GC-ed 되지 못하므로 주의를 요합니다. 이것 역시 위의 "2번"과 같은 문제로 결국 개발자가 잘못 프로그램을 한 경우인데, 가령 다음과 같은 식의 코드를 작성한다면,

```c#
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            for (int i = 0; i < 100; i++)
            {
                ConsoleHelper ch = new ConsoleHelper();
            }
        }
    }
}

public class ConsoleHelper
{
    static List _cmds = new List();

    public ConsoleHelper()
    {
        _cmds.Add(new ConsoleCommand());
    }
}

public class ConsoleCommand
{
}
```

static 변수에 보관된 _cmds의 인스턴스들은 GC가 절대 회수하지 못하므로 쉽게 메모리 누수가 발생할 수 있습니다. 개발자 입장에서 종종 실수하게 되는 부분인데, static 멤버 자체가 해당 클래스 내에 선언되므로 어느 순간 그것에 대한 관리를 소홀히 하게 될 여지로 인해 더욱 주의를 요합니다.




### 4. 잘못된 Cache 사용

원문을 정리하면, Cache 용도로 뭔가를 보관할 때, 1) 일정 시간 동안 사용하지 않으면 제거하고, 2) 캐시의 최대 용량을 설정하고, 3) WeakReference를 사용해 GC가 임의로 해제를 할 수 있게 만들라는 조언을 하고 있습니다.




### 5. 잘못된 WPF 바인딩 사용

오호... 재미있는 사실이군요. ^^ WPF 바인딩 대상이 INotifyPropertyChanged를 구현하지 않은 경우라면,

```xml
// xaml
<UserControl x:Class="WpfApp.MyControl"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <TextBlock Text="{Binding SomeText}"></TextBlock>
</UserControl>
```

// cs
```c#
public class MyViewModel
{
    public string _someText = "memory leak";
    public string SomeText
    {
        get { return _someText; }
        set { _someText = value; }
    }
}
```

WPF는 바인딩 소스에 대한 strong 참조를 유지하는 반면, 만약 INotifyPropertyChanged를 구현하고 있다면,

```c#
public class MyViewModel : INotifyPropertyChanged
{
    public string _someText = "not a memory leak";
 
    public string SomeText
    {
        get { return _someText; }
        set
        {
            _someText = value;
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nameof (SomeText)));
        }
    }

    // ...[생략]...
}
```

strong 참조를 하진 않는다고 합니다. 이러한 규칙은 Collection에 대한 INotifyCollectionChanged에 대해서도 동일하게 적용된다고 합니다. (암튼, ^^; WPF는 너무 복잡해서 알아둬야 할 규칙이 너무 많습니다.)

### 6. 종료하지 않는 Thread 사용

스레드가 종료하지 않으면, 적어도 해당 스레드의 콜 스택에 놓여진 참조들은 GC 대상이 될 수 없습니다. 원 글에서는 이에 대한 예제로, 스레드라고 자칫 인식하지 않을 수 있는 Timer를 예로 들고 있는데요,

```c#
public class MyClass
{
    public MyClass()
    {
        Timer timer = new Timer(HandleTick);
        timer.Change(TimeSpan.FromSeconds(5), TimeSpan.FromSeconds(5));
    }
 
    private void HandleTick(object state)
    {
        // do something
    }

    //...[생략]...
}
```

위에서 예를 든 Timer는 System.Threading.Timer로 전용 스레드가 생성되어 타이머 호출을 하는 경우입니다. 일단, 위와 같은 코드 상으로는 해당 스레드는 종료하지 않을 것이고, 여기서 "1. 잘못된 이벤트 핸들러 관리"였던 것과 겹쳐 HandleTick 인스턴스 핸들러로 인해 MyClass 인스턴스 자체가 GC가 불가능하게 됩니다.




### 7. 해제하지 못한 비관리 메모리

GC 구성 요소의 관리를 받지 못하는 비관리 메모리로부터 할당받은 메모리는 반드시 개발자가 직접 해제하는 코드를 작성해야 합니다. 예를 들어 아래와 같이 코드를 작성했다면,

```c#
public class SomeClass
{
    private IntPtr _buffer;
 
    public SomeClass()
    {
        _buffer = Marshal.AllocHGlobal(1000);
    }
 
    public void Dispose()
    {
        Marshal.FreeHGlobal(_buffer);
    } 
}
```

SomeClass를 사용하는 측에서는 반드시 Dispose 메서드까지 호출해야 합니다.

### 8. 필요한 경우 Finalizer 구현

Dispose 메서드의 호출은 해당 타입을 사용하는 개발자가 반드시 지켜줘야 하는 규칙이지만, 개발자들도 실수를 할 수 있기 때문에 이에 대한 대비도 해야 합니다. 이를 위해 Finalizer를 구현할 수 있는데요,

.NET IDisposable 처리 정리
; https://www.sysnet.pe.kr/2/0/347

그렇다고는 하지만, Finalizer의 잘못된 사용으로 인한 부작용도 있으므로 주의를 요합니다.

정리해 보면, 표면상으로는 "메모리 누수"라고는 해도 결국 "인스턴스"를 참조하고 있는 "또 다른 인스턴스"가 체인처럼 엮이면서 당연하게 발생하는 현상에 불과합니다. 이런 문제를 피하려면, 기본기를 충실히 익히고 자신이 사용하려는 환경에 대한 이해를 점점 넓혀가는 수밖에는 없을 듯합니다.

아울러, 시간 되시면 아래의 글도 한 번쯤 읽어보시고. ^^

WPF - WindowsFormsHost를 담은 윈도우 생성 시 메모리 누수
; https://www.sysnet.pe.kr/2/0/12340

windbg - 닷넷 응용 프로그램의 메모리 누수 분석
; https://www.sysnet.pe.kr/2/0/11808

윈도우 폼을 열고 닫는 것만으로 메모리 leak 이 발생할까?
; https://www.sysnet.pe.kr/2/0/1142

WPF의 Window 객체를 생성했는데 GC 수집 대상이 안 되는 이유
; https://www.sysnet.pe.kr/2/0/11310

C#에서 만든 COM 객체를 C/C++로 P/Invoke Interop 시 메모리 누수(Memory Leak) 발생
; https://www.sysnet.pe.kr/2/0/12162

ElementHost 컨트롤의 메모리 누수 현상
; https://www.sysnet.pe.kr/2/0/11027

### reference 

[C# - 닷넷 응용 프로그램에서 메모리 누수가 발생할 수 있는 패턴](https://www.sysnet.pe.kr/2/0/12343)  

