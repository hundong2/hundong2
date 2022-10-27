# 1. WPF Thread
C# 과 WPF 의 Thread 관리에 대해서 정리한 내용입니다.

## C#

기본적으로 Main Thread가 존재하며 추가로 System.Threading.Thread 클래스로 Thread를 생성합니다.  

C#에서의 스레드는 생성자(Constructor)에 실행하고자 하는 method를 delegate로 지정하며, 객체를 생성해 Start() method를 호출하여 만들 수 있습니다.

## WPF

모든 WPF 프로그램은 최소한의 렌더링을 위한 백그라운드 쓰레드 와 UI 스레드(UI 인터페이스 관리) 두개의 쓰레드로 기동됩니다.  
UI Thread 는 STA(Single-Threadded Apartment) Main Thread로, UI 관련 작업을 모두 수행합니다.  
즉, 사용자 입력을 받고 화면을 그리고, 코드를 실행하고, 이벤트등을 처리하는 스레드입니다.  
WPF의 Main Thread는 Dispatcher라는 클래스를 통해 Thread의 작업 수행을 Control 합니다.  
WPF Application의 Thread 마다 Dispatcher (System.Windows.Threading.Dispatcher) 가 존재하고,  
특정 Thread를 통해 UI 작업을 수행할 때는 해당 Thread의 Dispatcher에 요청해서 실행하는 방식으로 동작합니다.  

## 렌더링?

간단히 말해 UI를 구성하는 과정을 의미합니다.  
WPF는 기본적으로 STA(Single Thread Apartment) 모델을 지원하는데 하나의 Main 쓰레드는 전체 응용프로그램에서 실행되며 모든 WPF 객체를 소유합니다.  
그런데 TextBox같은 WPF UIElements 요소들은 다른 쓰레드와 상호작용 할 수 없도록 되어있습니다. (즉, 다른 쓰레드에서 UI를 업데이트 할 수가 없습니다.)  
이를 스레드 선호도라고 하고 멀티스레드 처리를 위해서는 Dispatcher 나 Background Worker를 사용해야 합니다.  

### 1.1. UI Thread와 작업 Thread

#### UI Thread

UI 컨트롤을 생성하고 이 컨트롤의 윈도우 핸들을 소유한 Thread로, WPF의 Main Thread 입니다.  
즉, UI 관련 작업을 모두 수행하는 Thread 입니다.  
다른 Thread에서 직접 접근이 불가능합니다.  

System.Windows.Threading.DispatcherObject를 통해 STA 사용  
STA (Single-Threadded Apartment) : 프로그램의 UI, 대부분의 메서드, 프로퍼티들을 동작시키는 Thread. 통상적으로 STA 객체는 하나의 Thread (보통 객체를 생성한 Thread) 에서만 엑세스가 가능.  

#### 작업 Thread
WPF의 멀티스레드 작업을 위해 만들어지는 Thread 입니다.  
Dispatcher를 이용해 UI Thread에 작업을 요청할 수 있습니다.  
1.2. Dispatcher를 이용한 WPF 멀티스레드 프로그래밍  
모든 비주얼 객체(TextBox, Button 등)는 DispatcherObject 클래스를 상속받고 있으며, DispatcherObject가 UI 스레드의 Dispatcher를 얻을 수 있게 해줍니다.  
이 Dispatcher 때문에 다른 스레드에서 UI 컨트롤을 직접 변경할 수 없고, Dispatcher를 거쳐서 수정해야하게 됩니다.  

#### Dispatcher

WPF 객체들을 독립적으로 관리하는 Queue 관리자  
System.Windows.Threading.Dispatcher 클래스의 인스턴스로 응용 프로그램 쓰레드를 소유(쓰레드에 속한 모든 개체를 소유)합니다.  
Dispatcher는 새 스레드를 만들지 않습니다. 즉, 멀티 스레드가 아닙니다.  
Dispathcer Queue 관리자의 작업 처리  
작업 항목의 대기열을 관리하는데 각각의 우선 순위를 사용하여 FIFO (First In First Out) 방식으로 UI 작업을 실행합니다.  

Queue의 작업 Frame (Work Item) 을 종료하기 전까지 UI 반영을 하지 않습니다.  
Queue의 작업단위가 마무리 되고나서 UI 반영합니다.  
문제점 : 특정 소스에서 바로 UI 반영이 필요할 경우, Main Thread가 Queue Frame을 종료하지 않은 채 UI 변경하려했을 때, 객체가 가진 값은 변경되었으나 UI에 반영되지 않습니다.  
해결방법 : Dispatcher, DispatcherObject 를 사용해서 반영해주어야합니다.  

#### DispatcherObject

DispatcherObject를 상속받는 클래스들은 외부로 노출되는 메서드나 프로퍼티에 대해서 이 두 메서드를 사용해서 STA를 실현하게 되어있습니다.  
WPF의 UI 관련 요소들은 대부분 DispatcherObject를 상속받습니다.  
DispatcherObject 에는 스레드를 판단하는 메서드가 있습니다.  
CheckAccess 메서드 : 코드가 객체를 사용할 수있는 스레드이면 true를 반환.  
VerifyAccess 메서드 : 코드가 객체를 사용하기 위해 올바른 스레드인지 판단.  
가능하다면 아무 작업도 수행하지 않고 그렇지 않으면 "InvalidOperationException"을 발생시킵니다.  

#### 1.2.1. Invoke / BeginInvoke
Dispatcher에 있는 메서드로, Dispatcher가 속해있는 Thread에서 Main Thread 로 작업을 요청하는 메서드입니다.  
Dispatcher가 요청받은 작업은 Work Item 이라고 하며, Dispatcher는 Main Thread 에서 작업될 Work Item 들을 우선순위 Queueing 합니다.  
예를 들어 여러개의 스레드에서 UI 작업을 각각 Invoke/BeginInvoke 로 요청했을 때 Work Item 들이 Dispathcer Queue에 담겨 우선순위에 따라 UI Thread에서 처리하게 되는 것입니다.  
Invoke : 컨트롤을 생성한 Thread에서 Dispatcher로 동기적으로 작업을 넘깁니다. 즉, 콜백이 반환 될 때까지 컨트롤이 호출 개체로 반환되지 않습니다.  
이곳 을 참고하시면 도움이 될 것입니다.  
BeginInvoke : 컨트롤을 생성한 Thread에서 Dispatcher로 비동기적으로 작업을 넘깁니다. 즉, 컨트롤이 호출 된 후에 호출하는 개체로 즉시 반환됩니다.  
이곳 을 참고하시면 도움이 될 것입니다.  
#### 1.2.2. CheckBeginInvokeOnUI / RunAsync (Dispatcher Helper)
WPF 에서 Dispatcher 를 편하게 활용할 수 있도록 만들어진 Dispatcher Helper 의 메서드 입니다.  

##### CheckBeginInvokeOnUI

UI Thread에서 호출: UI Thread 즉시 동기적으로 실행한다.  
작업 Thread에서 호출: Work Item이 UI Thread 대기열에 추가되고, 작업스레드와 비동기적으로 실행된다.
DispatcherHelper.CheckBeginInvokeOnUI(() => { });  

##### RunAsync

작업 Thread에서 호출: Work Item이 UI Thread 대기열에 추가되고, 작업스레드와 비동기적으로 실행된다.  
DispatcherHelper.RunAsync(() => { });  
CheckBeginInvokeOnUI 과 RunAsync 의 차이 : UI Thread에서 호출할 때, 동기/비동기 실행여부입니다.  
CheckBeginInvokeOnUI 를 호출하면 동기적으로 실행하기 때문에 UI에 반영이 끝나고 나서 반환됩니다.  
RunAsync를 호출하면 Dispatcher의 Queue에 WorkItem을 담고 바로 반환됩니다. 그리고는 작업을 이어갑니다.  
즉, 비동기로 실행되더라도 다음 실행되는 작업보다 UI에 반영되는 것이 늦어질 수 있습니다.  

## reference 

[dispatcher tbtb7 blog](https://tbtb7-sw.tistory.com/158#toc-WPF%20Thread)  