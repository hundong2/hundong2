# C++ for loop explanation

## 1. for loop ( old version )
```c++
for( int i = 0; i < 10; i++ )
    printf("hello world");
```

## 2. C++11 for loop
```c++
for(int i: {0, 1, 2, 3})
    std::cout << i << std::endl;

std::vector<std::string> mVector;
for(const auto& mValue : mVector)
{
    std::cout << mValue << endl;
}
```

## 3. std::for_each / #include<algorithm>
```c++
#include <iostream>
using namespace std;

vector<string> mVector{"abc", "def", "ghi"};
for_each(mVector.begin(), mVector.end(), [](auto& pValue)
{
    //to do...
    //example print mVector element
    cout << pValue << endl;
});
```

## 4. std::for_each_n / #include<algorithm>, C++17
<p>
first	-	the beginning of the range to apply the function to
n	-	the number of elements to apply the function to
policy	-	the execution policy to use. See execution policy for details.
f	-	function object, to be applied to the result of dereferencing every iterator in the range [first, first + n)
The signature of the function should be equivalent to the following:

void fun(const Type &a);

The signature does not need to have const &.
The type Type must be such that an object of type InputIt can be dereferenced and then implicitly converted to Type.
</p>

### Possible implementation
```c++
template<class InputIt, class Size, class UnaryFunction>
InputIt for_each_n(InputIt first, Size n, UnaryFunction f)
{
    for (Size i = 0; i < n; ++first, (void) ++i) {
        f(*first);
    }
    return first;
}
```

### Example 
```c++
#include <algorithm>
#include <iostream>
#include <vector>
 
int main()
{
    std::vector<int> ns{1, 2, 3, 4, 5};
    for (auto n: ns) std::cout << n << ", ";
    std::cout << '\n';
    std::for_each_n(ns.begin(), 3, [](auto& n){ n *= 2; });
    for (auto n: ns) std::cout << n << ", ";
    std::cout << '\n';
}
```
#### output 
```
1, 2, 3, 4, 5, 
2, 4, 6, 4, 5,
```

### site 
[std::ranges::for_each, std::ranges::for_each_result](https://en.cppreference.com/w/cpp/algorithm/ranges/for_each "range for_each")

[std::for_each_n](https://en.cppreference.com/w/cpp/algorithm/for_each_n "for_each_n")

[std::transform](https://en.cppreference.com/w/cpp/algorithm/transform "transfor")