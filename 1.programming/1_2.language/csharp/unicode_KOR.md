# unicode Korean UTF8 size problem
## Unicode 
- 언어 자체의 의미로 byte를 계산하려 하면
Unicode에서 인코딩해서 계산해야 한다.  
```csharp
string str = "안녕하세요";
byte[] data = Encoding.Default.Getbytes(str);
int count = data.Length; // count = 15
```

## explanation
- 기본적으로 System.Text.Encoding 클래스의 Default를 사용하면 UTF8 encoding을 사용.  
- UTF8 encoding의 경우 한글 1글자 당 3byte.  
- Unicode encoding 필요.  
```csharp
string str = "안녕하세요";
byte[] data = Encoding.Unicode.Getbytes(str);
int count = data.Length; // count = 10
```


