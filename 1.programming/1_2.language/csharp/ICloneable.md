# ICloneable Interface
## Expalnation
- Interface를 이용한 객체 복사


## example
트위스트를 사용하여 클래스에서 `ICloneable`을 구현합니다. 공개 유형에 안전한 `Clone()`을 노출하고 개체 `Clone()`을 비공개로 구현합니다.  
```csharp
public class Person : ICloneable
{
    // Contents of class
    public string Name { get; set; }
    public int Age { get; set; }
    // Constructor
    public Person(string name, int age)
    {
        this.Name=name;
        this.Age=age;
    }
    // Copy Constructor
    public Person(Person other)
    {
        this.Name=other.Name;
        this.Age=other.Age;
    }

    #region ICloneable Members
    // Type safe Clone
    public Person Clone() { return new Person(this); }
    // ICloneable implementation
    object ICloneable.Clone()
    {
        return Clone();
    }
    #endregion
}
```
다음과 같이 사용됩니다.  
```csharp
{
    Person bob=new Person("Bob", 25);
    Person bob_clone=bob.Clone();
    Debug.Assert(bob_clone.Name==bob.Name);

    bob.Age=56;
    Debug.Assert(bob.Age!=bob.Age);
}
```

`bob`의 나이를 변경해도 `bob_clone`의 나이는 변경되지 않습니다. 디자인이 (참조) 변수를 할당하는 대신 복제를 사용하기 때문입니다.

