# std::for_each ( c++20 )

## define 
Defined in header <algorithm>  
```c++
template< class InputIt, class UnaryFunction >
UnaryFunction for_each( InputIt first, InputIt last, UnaryFunction f ); //(until C++20)

template< class InputIt, class UnaryFunction >
constexpr UnaryFunction for_each( InputIt first, InputIt last, UnaryFunction f );//(since C++20)

template< class ExecutionPolicy, class ForwardIt, class UnaryFunction2 >
void for_each( ExecutionPolicy&& policy, ForwardIt first, ForwardIt last, UnaryFunction2 f );//(since C++17)
```
		
1) Applies the given function object f to the result of dereferencing every iterator in the range [first, last), in order.  
2) Applies the given function object f to the result of dereferencing every iterator in the range [first, last) (not necessarily in order). The algorithm is executed according to policy. This overload does not participate in overload resolution unless   
```c++
std::is_execution_policy_v<std::decay_t<ExecutionPolicy>> //(until C++20) 
std::is_execution_policy_v<std::remove_cvref_t<ExecutionPolicy>> //(since C++20) is true.
```
For both overloads, if the iterator type is mutable, f may modify the elements of the range through the dereferenced iterator. If f returns a result, the result is ignored.  

Unlike the rest of the parallel algorithms, for_each is not allowed to make copies of the elements in the sequence even if they are trivially copyable.  

## Parameters
`first, last`	-	the range to apply the function to   
`policy`	-	the execution policy to use. See execution policy for details.  
`f`	-	function object, to be applied to the result of dereferencing every iterator in the range [first, last) The signature of the function should be equivalent to the following:  
```c++
 void fun(const Type &a);
```
The signature does not need to have `const &`.  
The type `Type` must be such that an object of `type` InputIt can be dereferenced and then implicitly converted to Type.  

## Possible implementation
```c++ 
template<class InputIt, class UnaryFunction>
constexpr UnaryFunction for_each(InputIt first, InputIt last, UnaryFunction f)
{
    for (; first != last; ++first) {
        f(*first);
    }
    return f; // implicit move since C++11
}
```
## Example 1 
The following example uses a lambda function to increment all of the elements of a vector and then uses an overloaded operator() in a functor to compute their sum. Note that to compute the sum, it is recommended to use the dedicated algorithm `std::accumulate`.  
```c++
#include <vector>
#include <algorithm>
#include <iostream>
 
struct Sum
{
    void operator()(int n) { sum += n; }
    int sum{0};
};
 
int main()
{
    std::vector<int> nums{3, 4, 2, 8, 15, 267};
 
    auto print = [](const int& n) { std::cout << " " << n; };
 
    std::cout << "before:";
    std::for_each(nums.cbegin(), nums.cend(), print);
    std::cout << '\n';
 
    std::for_each(nums.begin(), nums.end(), [](int &n){ n++; });
 
    // calls Sum::operator() for each number
    Sum s = std::for_each(nums.begin(), nums.end(), Sum());
 
    std::cout << "after: ";
    std::for_each(nums.cbegin(), nums.cend(), print);
    std::cout << '\n';
    std::cout << "sum: " << s.sum << '\n';
}
```
### Output
```bash
before: 3 4 2 8 15 267
after:  4 5 3 9 16 268
sum: 305
```

## Eaxample 2
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
[cppreference.com](https://en.cppreference.com/w/cpp/algorithm/for_each "for_each")
