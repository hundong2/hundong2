# get,set attribute

- GET, SET 메서드를 가지는 클래스 내부 변수( 보통 PRIVATE로 선언 )를 class의 attribute라 부른다. 
- c#의 class내 변수 접근법

## c++ 일반적인 표현
```c++
class Person
{
  int age;
  public:
    int get_age() const { return age; }
    void set_age(int value) { age = value; }
```

## Explanation

- 많은 프로그래밍 언어들에서 ( C#, kotlin ... )에서 속성을 언어자체에서 내장, 제공한다. 
- C++은 내장 지원 없음. 
- 단, 비표준적인 방법으로 지원 (MSVC, Clang, Intel)

### example
```c++
class Person
{
  int age_;
  public: 
    int get_age() const { return age_; }
    void set_age(int value) { age_ = value; }
    __declspec(property(get=get_age, put=set_age)) int age;
};
```
```c++
Person person;
p.age = 20; // call p.set_age(20)
```
