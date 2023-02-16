# Class 

## 다중 상속

- Person이 겹치는 다이아몬드 상속을 문제를 해결 할 수 있는 방법.
- 대신 Person, Me, Wife 생성자를 호출 해야 된다. 

```c++
class Person {
    public :
        ...
}

class Me : public virtual Person 
{
    // ...
}
class Wife : public virtual Person 
{
    // ...
}
class Our : public Me, public Wife
{
    // ...
}
```