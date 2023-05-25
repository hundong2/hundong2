# C++ 유용한 기능 정리

## 개행 문자 제거

```c++
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string str = "안녕하세요.\n반갑습니다.";

    // 개행 문자(\n) 제거
    str.erase(std::remove(str.begin(), str.end(), '\n'), str.end());

    std::cout << str << std::endl;  // 출력: 안녕하세요.반갑습니다.

    return 0;
}
```
