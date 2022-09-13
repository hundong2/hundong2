# aggregate 

## Aggregate initialization

- 배열, 클래스(구조체)를 초기화 할 때 "중괄호를 사용해서 요소(멤버)들을 초기화" 하는것. 
- 클래스(구조체)를 "aggregate initialization"으로 초기화 하려면
    - no private or protected non-static data members 
    - no user-declared or inherited constructors
    - no virtual, private, or protected base classes
    - no virtual member functions

## std::is_aggregate ( C++17 )

- 주어진 타입이 "aggregate type" 인지를 조사. 

