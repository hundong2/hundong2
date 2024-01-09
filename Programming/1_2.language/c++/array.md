# array class 
## definition
- 길이가 N인 Ty 형식의 요소 시퀀스를 제어하는 개체를 설명합니다. 시퀀스는 array<Ty, N> 개체에 포함된 Ty의 배열로 저장됩니다.  

```c++
template <class Ty, std::size_t N>
class array;
```

## parameter 
Ty  요소의 형식입니다.  
N  요소의 수입니다.  

## explanation
형식에 기본 생성자 array()와 기본 대입 연산자 operator=가 있고 aggregate에 대한 요구 사항을 충족합니다. 따라서 집계 이니셜라이저를 사용하여 array<Ty, N> 형식의 개체를 초기화할 수 있습니다. 예를 들면 다음과 같습니다.  
```c++
array<int, 4> ai = { 1, 2, 3 };
```
4개의 정수 값을 보유하는 ai 개체를 만들고, 처음 세 개의 요소를 값 1, 2, 3으로 각각 초기화한 다음 네 번째 요소를 0으로 초기화합니다.  

## example 
```c++
#include <iostream>
#include <array> //array
#include <algorithm> //for_each

using namespace std;
typedef array<int, 4> Myarray;

int main()
{
    Myarray mArr = { 1,2,3,4};
    for_each(mArr.begin(), mArr.end(), []<typename T>(T input){
       cout << input << endl; 
    });

    return 0;
}
```

## reference 
[Online compiler](https://www.onlinegdb.com/online_c++_compiler#)  
[modoocode](https://modoocode.com/314)  




