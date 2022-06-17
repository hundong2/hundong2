# What is Annotation?

## Annotation 
<p>
애노테이션은 자바 소스 코드에 추가 할 수있는 메타 데이터의 한 형태입니다. 
클래스, 인터페이스, 메소드, 변수, 매개 변수 등에 추가 할 수 있습니다. 애노테이션은 소스 파일에서 읽을 수도 있고, 
컴파일러에 의해 생성된 클래스 파일에 내장되어 읽힐 수도 있으며, 
Runtime에 Java VM에 의해 유지되어 리플렉션에 의해 읽어 낼 수도 있습니다.
</p>

## Annotation 종류
<p>
- @Override 어노테이션을 사용하여 메소드를 재정의.
- @Singleton 싱글톤 패턴을 사용
- 기타... @NonNull, @StringRes, @IntRes 등
</p>

## Why Annotation?

1. Speed 
    - javac의 일부이므로 모든 처리가 run time보다는 compile time에 발생. 
2. No Use [Reflection](#reflection)
    - 자바의 리플렉션은 런타임에 많은 예외를 발생시킵니다. 어느 누구도 예외처리를 많이 하는것을 원치는 않습니다. 또한 리플렉션을 비용이 큰 작업이며, Annotation Processor는 리플렉션이 없이 프로그램의 의미 구조를 알수 있게 해줍니다.
3. [Boilerplate code](boilerplate_code.md)를 생성해줍니다. 
    - Annotation Processor를 사용하는 가장 큰 이유이자 유용한 기능은 바로 보일러플레이트 코드 생성입니다. ButterKnife, Room, Retrofit등 많은 라이브러리들이 반복되는 지루한 코드로부터 벗어나고자 애노테이션을 사용하고 있습니다.



### Reflection?
- 자바 언어의 기능중 하나, 프로그램 내부 속성을 조작할 수 있다. 
- `using System;` , `using System.Reflection;`을 .cs에 추가해야된다. 
<p>
리플렉션은 어셈블리, 모듈 및 형식을 설명하는 개체(Type 형식)를 제공합니다. 리플렉션을 사용하면 동적으로 형식 인스턴스를 만들거나, 형식을 기존 개체에 바인딩하거나, 기존 개체에서 형식을 가져와 해당 메서드를 호출하거나, 필드 및 속성에 액세스할 수 있습니다. 코드에서 특성을 사용하는 경우 리플렉션은 특성에 대한 액세스를 제공합니다. 자세한 내용은 특성을 참조하세요.

다음은 GetType() 메서드(Object 기본 클래스의 모든 형식에 상속됨)를 사용하여 변수 형식을 가져오는 간단한 리플렉션 예제입니다.
</p>

```cs
// Using GetType to obtain type information:
int i = 42;
Type type = i.GetType();
Console.WriteLine(type);
```
출력은 `System.Int32` 입니다. 

참고사이트/출처: [microsoft](https://docs.microsoft.com/ko-kr/dotnet/csharp/programming-guide/concepts/reflection "reflection")