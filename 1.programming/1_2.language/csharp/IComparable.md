# IComaparable Interface

## definition
- namespace : System  
- Assembly : System.Runtime.dll  
```csharp
public interface IComparable
```
```csharp
interface IComparable  //  IComparable의 I는 인터페이스를 뜻하며, 인터페이스는 반드시 구현해야하는 클래스이다.
{

   int CompareTo(object obj);

}
```

IComparable 필수 Interface function  
-> `CompareTo` 메서드. 

-  C#의 컬렉션은 대부분 Sort메서드를 제공하는데 다음과 같이 IComparable 인터페이스를 구현해야 정상적으로 동작한다.   - IComparable 인터페이스는 자신과 비교할 매개변수를 비교하여 결과를 반환하는 `CompreTo` 메서드를 만들도록 약속하고있다.  - 매개 변수 형식이 object 형식으로 되어 있으므로 프로그램 목적에 맞게 캐스팅하여 처리해야 한다.

## Example


```csharp
class Member : IComparable
        {
            public string Name;
            public int Age;
            public string Gender;

            // sort function에서 호출 되는 함수. 
            public int CompareTo(object obj)
            {
                Member mMember = (Member)obj;  // obj 객체생성
                return this.Age.CompareTo(mMember.Age); // age arrangement
            }
            public override string ToString()
            {
                return string.Format($"[{Name},{Age},{Gender}]");
            } 
        }
```

