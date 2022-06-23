# C++ find function

## std::find 
```c++
template <class InputIterator, class T>
   InputIterator find (InputIterator first, InputIterator last, const T& val);
```

## find value in range

Returns an iterator to the first element in the range [first,last) that compares equal to val. If no such element is found, the function returns last.  

The function uses operator== to compare the individual elements to val.  

The behavior of this function template is equivalent to:  
```c++
template<class InputIterator, class T>
  InputIterator find (InputIterator first, InputIterator last, const T& val)
{
  while (first!=last) {
    if (*first==val) return first;
    ++first;
  }
  return last;
}
```

## parameter 

> first, last  

Input iterators to the initial and final positions in a sequence. The range searched is [first,last), which contains all the elements between first and last, including the element pointed by first but not the element pointed by last.  

> val  

Value to search for in the range.
T shall be a type supporting comparisons with the elements pointed by InputIterator using operator== (with the elements as left-hand side operands, and val as right-hand side).  

## Return value 

An iterator to the first element in the range that compares equal to val.
If no elements match, the function returns last.  

## Example 
```c++
// find example
#include <iostream>     // std::cout
#include <algorithm>    // std::find
#include <vector>       // std::vector

int main () {
  // using std::find with array and pointer:
  int myints[] = { 10, 20, 30, 40 };
  int * p;

  p = std::find (myints, myints+4, 30);
  if (p != myints+4)
    std::cout << "Element found in myints: " << *p << '\n';
  else
    std::cout << "Element not found in myints\n";

  // using std::find with vector and iterator:
  std::vector<int> myvector (myints,myints+4);
  std::vector<int>::iterator it;

  it = find (myvector.begin(), myvector.end(), 30);
  if (it != myvector.end())
    std::cout << "Element found in myvector: " << *it << '\n';
  else
    std::cout << "Element not found in myvector\n";

  return 0;
}
```

### Output 
```bash
Element found in myints: 30
Element found in myvector: 30
```

## reference 

[cplusplus.com](https://cplusplus.com/reference/algorithm/find/)  
