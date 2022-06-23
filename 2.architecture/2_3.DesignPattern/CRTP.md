# CRTP ( Curiously Recurring Template Pattern )

- 자기 자신을 베이스 클래스의 템플릿 인자로 상속. 
- 베이스 클래스의 구현부에서 타입이 지정된 this 포인터를 사용할 수 있게 된다. 

## Example code 1
```c++ 
template <typename Derived> 
class CuriousBase { 
    … 
};

class Curious : public CuriousBase<Curious> { 
    … 
};
```

## Example code 2 
### Template 
```c++
#include <stddef.h>

template <typename CountedType> 
class ObjectCounter { 
  private: 
    static size_t count;    // 존재하는 객체 수

  protected: 
    // 기본 생성자
    ObjectCounter() { 
        ++ObjectCounter<CountedType>::count; 
    }

    // 복사 생성자 
    ObjectCounter (ObjectCounter<CountedType> const&) { 
        ++ObjectCounter<CountedType>::count; 
    }

    // 소멸자
    ~ObjectCounter() { 
        --ObjectCounter<CountedType>::count; 
    }

  public: 
    // 존재하는 객체 수를 반환 
    static size_t live() { 
        return ObjectCounter<CountedType>::count; 
    } 
};

// 카운터를 0으로 초기화
template <typename CountedType> 
size_t ObjectCounter<CountedType>::count = 0;
```

### Execute code
```c++
#include "objectcounter.hpp" 
#include <iostream>

template <typename CharT> 
class MyString : public ObjectCounter<MyString<CharT> > { 
  … 
};

int main() 
{ 
    MyString<char> s1, s2; 
    MyString<wchar_t> ws; 
    std::cout << "number of MyString<char>: " 
              << MyString<char>::live() << std::endl; 
    std::cout << "number of MyString<wchar_t>: " 
              << ws.live() << std::endl; 
}
```

## reference 
[3 묘하게 되풀이되는 템플릿 패턴(CRTP)](https://wikidocs.net/book/1)  

