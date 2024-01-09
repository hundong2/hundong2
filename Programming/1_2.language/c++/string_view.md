# string_view ( from. C++17 )

## Explanation

- 다양한 문자열 타입을 전달 받을 수 있는 안전하고, 효과적인 방법을 제공.  
- 문자열에 대한 Pointer와 길이만 가짐.  
- string_view는 내부적으로 null 종료 문자를 가지지 않음.   
- 원본 데이터에 대한 변경 방지.  
- 원본 데이터에 대한 객체의 수명을 조절 할 수 없음. ( 호출하는 주체가 원본데이터의 안전성을 보장해야 함. )

| name              | explanation                       |
|:---               |:---                               |
|string_view        | std::basic_string_view<char>      |
|wstring_view       | std::basic_string_view<wchar_t>   |   
|u16string_view     | std::basic_string_view<char16_t>  |   
|u32string_view     | std::basic_string_view<char32_t>  |
|u8string_view(C++20)| std::basic_string_view<char8_t>   |

## Example 1
```c++
#include <iostream>
#include <string_view>
 
int main() {
    constexpr std::string_view unicode[] {
        "▀▄─", "▄▀─", "▀─▄", "▄─▀"
    };
 
    for (int y{}, p{}; y != 6; ++y, p = ((p + 1) % 4)) {
        for (int x{}; x != 16; ++x)
            std::cout << unicode[p];
        std::cout << '\n';
    }
}
```
### Output 
```bash
▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─
▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─
▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄
▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀
▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─▀▄─
▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─▄▀─
```

## Example 2
```c++
// c++ 14버전
std::string FiveCharacterOnlyString(const std::string & str)
{
    if (str.size() < 5) return str;
    return str.substr(0, 5);
}

// c++ 17 string_view
// string_view를 사용하면 string 객체의 복사가 발생하지 않습니다. 
std::string_view FiveCharacterOnlyStringView(const std::string_view str)
{
    if (str.size() < 5) return str;
    return str.substr(0, 5);
}

// std::string val1 = "12345"
auto val1 = FiveCharacterOnlyString("123456789");
// std::string_view val2 = "12345"
auto val2 = FiveCharacterOnlyStringView("123456789");
```

## Example 3
```c++
void CallerOriginStringObject(std::string_view str_v, std::string& str)
{
    std::cout << "[origindata] str_v = " << str_v.data() << " Size = " << str_v.size() << std::endl;
    str = "modify";
    // 원본데이터가 변경되면 string_view의 데이터가 변경됩니다.
    // 문자열 : "modify", size = 15
    // 남아있는 빈 공간에는 이전 데이터가 들어 있습니다. 
    std::cout << "[origindata modify] str_v = " << str_v.data() << " Size = " << str_v.size() << std::endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
    std::string str("original string");
    CallerOriginStringObject(str, str);
}
```

## reference 
[[c++] string_view - jungwoong blog](https://jungwoong.tistory.com/56)  

[basic_string_view - cppreference.com](https://en.cppreference.com/w/cpp/string/basic_string_view)  




