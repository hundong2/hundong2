# C++ value category 

## blog seuulgi

C++11이 나오기 전, C++의 value category는 lvalue와 rvalue만으로 이루어진 단순한 분류체계를 가지고 있었다. 하지만 C++11이 나오면서 xvalue, glvalue, prvalue가 추가되면서 복잡한 분류체계를 가지게 됐다. 이번 글에서는 C++11에서 변경된 value category에 대해서 알아보도록 하겠다.

### until c++03

 C++11에서 새로 추가된 value들을 알기 전에 C++03 이전에도 있었던 lvalue와 rvalue가 뭔지부터 확실히 하고 넘어가야 한다. 흔히들 많이 실수하는 것이 lvalue는 assign operator(operator =)의 왼쪽에 올 수 있는 값이고, rvalue는 올 수 없는 값이라고 생각하는 것이다. C에서 lvalue라는 개념이 처음 나왔던 시절에는 assign operator를 기준으로 lvalue인지 아닌지를 구분하는 것이 맞았다. 하지만 C89에서 const 한정자가 추가되면서 더는 맞지 않다. const variable은 lvalue이지만 assign operator의 왼쪽에 올 수 없기 때문이다.
 따라서 C89에서는 lvalue를 left value가 아닌 locator value. 즉, 실제 값이 아닌 값이 있는 주소를 지칭하는 locator value라고 정의했다. 즉, 변수는 locator이기 때문에 lvalue이고, 1, 2 같은 숫자 리터럴이나 'a', 'b' 같은 문자 리터럴, 혹은 함수의 실행 결괏값 같은 경우 특정한 주소를 지칭하는 locator가 아니므로 lvalue가 아니다. 이 중에서 const 한정자가 붙지 않은 경우를 modifiable lvalue라고 따로 분류하여, modifiable lvalue만 assign operator의 왼쪽에 올 수 있다. 후에 나온 C++98도 C89의 lvalue 정의를 따랐기 때문에 C++98에서의 lvalue도 locator 라고 보면 된다. 다만 C89와 다르게 레퍼런스를 리턴하는 함수가 존재하기 때문에, 함수의 결과 타입이 레퍼런스일 경우, 함수의 실행 결과가 lvalue가 된다.

### identity

 C++11에서는 기존의 lvalue가 가지는 특성을 identity를 가진다고 표현한다. 어떤 expression이 identity를 가진다고 하면 그 expression은 다른 expression이 표현하는 것이 같은 것(원문은 entity라고 하는데 이를 표현할 번역을 못 찾았다.)인지 비교할 수 있다는 것을 의미한다. 예를 들어 a라는 변수와 b라는 변수가 있으면 이 둘은 주소를 비교해서 같은 값을 가리키는지 아닌지 비교할 수 있으니 변수는 lvalue이다. 하지만 숫자 literal이나 boolean literal은 두 expression이 같은 entity인지 비교할 수 없기 때문에 rvalue이다. 또한 리턴 타입이 레퍼런스가 아닌 함수의 실행이나 타입 캐스팅같이 임시값으로 해당 expression이 넘어가면 사라지는 임시값들도 rvalue이다. 즉, lvalue의 경우 expression이 넘어서까지 entity가 존재하는 expression이기 때문에 identity를 가진다는 것을 persistence가 있다고 표현하기도 한다.

### move

 C++11에서는  identity 말고 한 가지 특성이 더 추가됐다. C++11의 새 기능 중 가장 유명한 move가 추가됐기 때문이다. 모든 값이 move 될 수 있는 것은 아니기 때문에 이제 C++에서는 어떤 값이 다른 값으로 move 될 수 있는지 아닌지도 매우 중요한 특성이 됐다.
 이제부터 어떤 값이 move 될 수 있으면 m, move 될 수 없으면 M이라고 부르겠다. 또한, 앞에서 설명한 identity를 가지는 경우 이 값을 i, identity를 가지지 않는 경우 I라고 부른다. 이 identity를 가지는지와 move 될 수 있는지를 조합하면 iM, im, Im, IM 4가지 조합이 나온다. 하지만 이 중 IM. 즉, identity를 가지지도 않고, move 될 수도 없는 값은 있을 필요가 없으므로 우리는 iM, im, Im 3가지 조합만 살펴보면 된다.

### iM - lvalue

 iM. 즉, identity를 가지지만, move 될 수도 없는 expression을 C++11에서는 lvalue라고 부른다. C++03까지의 lvalue 정의에 move 될 수 없다는 조건이 더 추가된 것이다. lvalue의 가장 큰 특징은 lvalue만이 & operator의 피연산자로 사용될 수 있다는 것이다, Im은 identity를 가지지 않기 때문에, iM은 move 돼 버릴 수 있으므로 & operator의 피연산자로 사용될 수 없다.

im - xvalue
 identity를 가지지만 move 될 수 있는 im의 경우는 eXpiring에서 따와 xvalue라고 부른다. xvalue는 이름 그대로 만료되어 가는 값이다. 따라서 expression이 끝나고 expression이 의미하던 주소로 접근했을 때 값이 존재할 수도 있고, 존재하지 않을 수도 있다. rvalue reference를 리턴하는 함수의 결괏값이나 rvalue rference로 타입 캐스팅 하는 expression이 xvalue에 해당한다. std::move도 rvalue reference를 리턴하는 함수이기 때문에 무언가를 move한 값은 xvalue에 속하고, lvalue를 move할 수 있게 만드는데 사용된다.

Im - prvalue
 마지막으로 identity를 가지지 않는 Im은 pure rvalue라는 의미에서 prvalue라고 부른다. 이는 C++03까지의 rvalue와 같다고 봐도 무방하다. prvalue는 C++에서 유일하게 identity를 가지지 않는다. non-reference를 리턴하는 함수의 실행결과나 non-reference로의 타입 캐스팅 혹은 숫자 boolean 리터럴들이 여기에 속한다.
 또한, identity를 가지지 않는다는 특성 때문에 prvalue는 다른 값들과 다르게 incomplete type일 수 없다. expression이 사용되는 시점에서 값이 존재해야 하기 때문이다.

m - rvalue
 Im이 rvalue가 아니라 pure rvalue인 이유는 rvalue가 따로 있기 때문이다. C++03 이전에는 identity를 가지지 않는 값을 rvalue라고 불렀지만, C++11에서는 m. 즉, move될 수 있는 값을 rvalue라고 부른다. 그래서 im인 xvalue와 Im인 prvalue 둘은 rvalue에 속하고, move될 수 없는 im, lvalue는 rvalue가 아니다.

i - glvalue
 move 될 수 있는지를 기준으로 lvalue와 rvalue를 나누듯이 identity를 가지는지 아닌지로 glvalue와 prvalue를 나눈다. 그래서 iM(lvalue)와 im(xvalue)는 glvalue로 분류된다. identity를 가진다는 것은 해당 expression이 끝나도 object는 남아있다는 것이고, 이 expression은 그저 object를 가리키는 무언가일 뿐이라는 것이다. 그래서 glvalue에 속하는 lvalue나 rvalue는 incomplete 한 타입일 수 있고, polymorphic 할 수도 있다.

 [슭의 개발 블로그](https://blog.seulgi.kim/2017/06/cpp11-value-category.html)  
 