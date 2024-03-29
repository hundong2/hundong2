# programming TIP

- [programming TIP](#programming-tip)
  * [01. string, list 중복 제거 ( 정렬 없이 그대로 )](#01-string--list--------------------)
  * [02. array 2차원 초기화](#02-array-2------)
    + [leetcode example 2373. Largest Local Values in a Matrix](#leetcode-example-2373-largest-local-values-in-a-matrix)
  * [03. dictionary value 값에 따라 sort](#03-dictionary-value-------sort)
  * [04. for loop](#04-for-loop)
    + [4.1 for range](#41-for-range)
    + [4.2 for reversed range](#42-for-reversed-range)
  * [05. List](#05-list)
    + [5.1 List strint to integer convert](#51-list-strint-to-integer-convert)
  * [06. heapq](#06-heapq)
    + [6.1 heapq algorithm](#61-heapq-algorithm)
  * [07. string](#07-string)
      - [7.1 string count](#71-string-count)
      - [7.2 removesuffix](#72-removesuffix)
      - [7.3 replace](#73-replace)
      - [7.4 Position](#74-position)
      - [7.5 rfind](#75-rfind)
      - [7.6 find](#76-find)
  * [08. itertools](#08-itertools)
    + [8.1 combinations()](#81-combinations--)
    + [8.2 combinations_with_replacement()](#82-combinations-with-replacement--)
    + [8.3 product()](#83-product--)
    + [8.4 permutations()](#84-permutations--)
    + [reference](#reference)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 01. string, list 중복 제거 ( 정렬 없이 그대로 )

- set만 사용하면 정렬 한 값이 output  

```python
def func_example(self, s: str):
    list_str = list(dict.fromkeys(list(s)))
    return list_str
```

## 02. array 2차원 초기화

### leetcode example 2373. Largest Local Values in a Matrix

[2373. Lorgest Local Values in a Matrix](https://leetcode.com/problems/largest-local-values-in-a-matrix/)  

```python
value = [(-1,-1), (-1,0),(1,0) ,(-1,1), (0,-1), (1,-1), (0,1), (1,1), (0,0)]
class Solution:
    def check(self, grid, row, col):
        mlength = len(grid)
        max_val = 0
        for r, c in value:
            if row + r >= 0 and row + r < mlength and col + c >= 0 and col + r < mlength:
                max_val = max(max_val, grid[row + r][col + c])
        return max_val
    
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        return_val = list()
        for r in range(length - 2):
            temp = []
            for c in range(length - 2):
                temp.append(self.check(grid,r + 1, c + 1))
                print(r+1,c+1,temp)
                
            
            return_val.append(temp)
        return return_val
```

## 03. dictionary value 값에 따라 sort 

[leetcode 1338 Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/)  

```python
class Solution:
    def test(self, arr):
        if len(arr) == len(set(arr)):
            return False
        else:
            return True
    def minSetSize(self, arr: List[int]) -> int:
        #exception handling last time limited 
        if not self.test(arr):
            print("check OK")
            return (int)(len(arr)/2)
        set_val = {}
        print(len(arr))
        for _ in set(arr):
            set_val[_] = arr.count(_)
        sorted_dic = sorted(set_val.items(), key = lambda item: item[1], reverse = True)
        
        count_val = 0
        sum_val = 0
        for k, v in sorted_dic:
            count_val += 1
            sum_val += v
            #print(count_val, sum_val, v, (int)(len(arr)/2), len(arr) - sum_val)
            if len(arr) - sum_val <= (int)(len(arr)/2):
                return count_val
        return 0
```

## 04. for loop 

### 4.1 for range

```python
for _ in range(0, n):
    print(_) #print integer value ( 0 ~ n - 1 )
```

### 4.2 for reversed range

```python
for _ in reversed(range(0, n)):
    print(_) # print integer value ( n - 1 ~ 0 )
```

## 05. List

### 5.1 List strint to integer convert 

```python 
# list_val = ["1","2","3","4","5"] to convert list_val = [1,2,3,4,5] 
list_val = map(int,list_val) #python2
list_val = list(map(int,list_val))
```

## 06. heapq

### 6.1 heapq algorithm 

[heapq algorithm](https://docs.python.org/ko/3/library/heapq.html)  


## 07. string 

#### 7.1 string count 

```python
strvalue = "abcdef"
strvalue.count('a') # 1

str = "Hello World"
>>> str.count('o',0,5)
1
```

#### 7.2 removesuffix 

```python
>>> text = 'Quickly'
>>> print(text.removesuffix('ly'))
Quick
>>> print(text.removesuffix('World'))
Quickly
```

#### 7.3 replace 

```python
>>> list_str = {'Abc.ex', 'Bcd.ex', 'cde.ex', 'def.jpg', 'efg.jpg'}
>>> new_set = {x.replace('.ex', '').replace('.jpg', '') for x in list_str}
>>> print(new_set)
{'Bcd', 'Abc', 'def', 'efg', 'cde'}
```  

- string.replace('이전값', '새 값', '개수')

```python
>>> text = "Hello World!"
>>> x = text.replace("l", "k", 1)
>>> print(x)
```
#### 7.4 Position

```python
>>> text = 'Welcome to Codetorial'
>>>
>>> pos_e = text.index('e')
>>> print(pos_e)
1

>>> pos_Code = text.index('Code')
>>> print(pos_Code)
11
>>>
```

#### 7.5 rfind

```python
text = 'Welcome to Codetorial'

pos_e_last = text.rfind('e')
print(pos_e_last)

14
```

#### 7.6 find

```python
text = 'Welcome to Codetorial'

pos_e = text.find('e')
print(pos_e)
```


## 08. itertools 

### 8.1 combinations()

- iterable에서 원소 개수가 n개 인 조합 뽑기

```python
>>> from itertools import combinations
>>>
>>> combi = [1,2,3,4]
>>> for i in combinations(combi,2):
...    print(i)
...
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
>>>    
```

### 8.2 combinations_with_replacement()

- 원소 개수가 r개인 중복 조합 뽑기 

```python
>>> from itertools import combinations_with_replacement
>>> iter = ['jisu','jennie', 'lisa', 'rose']
>>> for i in combinations_with_replacement(iter,2):
...    print(i)
...
('jisu', 'jisu')
('jisu', 'jennie')
('jisu', 'lisa')
('jisu', 'rose')
('jennie', 'jennie')
('jennie', 'lisa')
('jennie', 'rose')
('lisa', 'lisa')
('lisa', 'rose')
('rose', 'rose')
```
### 8.3 product()

- 데카르트 곱 

```python
>>> from itertools import product
>>> for i in product(iter[0:2],iter[2:],repeat=1):
...    print(i)
...
('jisu', 'lisa')
('jisu', 'rose')
('jennie', 'lisa')
('jennie', 'rose')


>>> for i in product(iter[0:2],iter[2:],repeat=3):
...    print(i)
...
('jisu', 'lisa', 'jisu', 'lisa', 'jisu', 'lisa')
('jisu', 'lisa', 'jisu', 'lisa', 'jisu', 'rose')
('jisu', 'lisa', 'jisu', 'lisa', 'jennie', 'lisa')
('jisu', 'lisa', 'jisu', 'lisa', 'jennie', 'rose')
('jisu', 'lisa', 'jisu', 'rose', 'jisu', 'lisa')
('jisu', 'lisa', 'jisu', 'rose', 'jisu', 'rose')
('jisu', 'lisa', 'jisu', 'rose', 'jennie', 'lisa')
('jisu', 'lisa', 'jisu', 'rose', 'jennie', 'rose')
('jisu', 'lisa', 'jennie', 'lisa', 'jisu', 'lisa')
('jisu', 'lisa', 'jennie', 'lisa', 'jisu', 'rose')
('jisu', 'lisa', 'jennie', 'lisa', 'jennie', 'lisa')
('jisu', 'lisa', 'jennie', 'lisa', 'jennie', 'rose')
('jisu', 'lisa', 'jennie', 'rose', 'jisu', 'lisa')
('jisu', 'lisa', 'jennie', 'rose', 'jisu', 'rose')
('jisu', 'lisa', 'jennie', 'rose', 'jennie', 'lisa')
('jisu', 'lisa', 'jennie', 'rose', 'jennie', 'rose')
('jisu', 'rose', 'jisu', 'lisa', 'jisu', 'lisa')
('jisu', 'rose', 'jisu', 'lisa', 'jisu', 'rose')
('jisu', 'rose', 'jisu', 'lisa', 'jennie', 'lisa')
('jisu', 'rose', 'jisu', 'lisa', 'jennie', 'rose')
('jisu', 'rose', 'jisu', 'rose', 'jisu', 'lisa')
('jisu', 'rose', 'jisu', 'rose', 'jisu', 'rose')
('jisu', 'rose', 'jisu', 'rose', 'jennie', 'lisa')
('jisu', 'rose', 'jisu', 'rose', 'jennie', 'rose')
('jisu', 'rose', 'jennie', 'lisa', 'jisu', 'lisa')
('jisu', 'rose', 'jennie', 'lisa', 'jisu', 'rose')
('jisu', 'rose', 'jennie', 'lisa', 'jennie', 'lisa')
('jisu', 'rose', 'jennie', 'lisa', 'jennie', 'rose')
('jisu', 'rose', 'jennie', 'rose', 'jisu', 'lisa')
('jisu', 'rose', 'jennie', 'rose', 'jisu', 'rose')
('jisu', 'rose', 'jennie', 'rose', 'jennie', 'lisa')
('jisu', 'rose', 'jennie', 'rose', 'jennie', 'rose')
('jennie', 'lisa', 'jisu', 'lisa', 'jisu', 'lisa')
('jennie', 'lisa', 'jisu', 'lisa', 'jisu', 'rose')
('jennie', 'lisa', 'jisu', 'lisa', 'jennie', 'lisa')
('jennie', 'lisa', 'jisu', 'lisa', 'jennie', 'rose')
('jennie', 'lisa', 'jisu', 'rose', 'jisu', 'lisa')
('jennie', 'lisa', 'jisu', 'rose', 'jisu', 'rose')
('jennie', 'lisa', 'jisu', 'rose', 'jennie', 'lisa')
('jennie', 'lisa', 'jisu', 'rose', 'jennie', 'rose')
('jennie', 'lisa', 'jennie', 'lisa', 'jisu', 'lisa')
('jennie', 'lisa', 'jennie', 'lisa', 'jisu', 'rose')
('jennie', 'lisa', 'jennie', 'lisa', 'jennie', 'lisa')
('jennie', 'lisa', 'jennie', 'lisa', 'jennie', 'rose')
('jennie', 'lisa', 'jennie', 'rose', 'jisu', 'lisa')
('jennie', 'lisa', 'jennie', 'rose', 'jisu', 'rose')
('jennie', 'lisa', 'jennie', 'rose', 'jennie', 'lisa')
('jennie', 'lisa', 'jennie', 'rose', 'jennie', 'rose')
('jennie', 'rose', 'jisu', 'lisa', 'jisu', 'lisa')
('jennie', 'rose', 'jisu', 'lisa', 'jisu', 'rose')
('jennie', 'rose', 'jisu', 'lisa', 'jennie', 'lisa')
('jennie', 'rose', 'jisu', 'lisa', 'jennie', 'rose')
('jennie', 'rose', 'jisu', 'rose', 'jisu', 'lisa')
('jennie', 'rose', 'jisu', 'rose', 'jisu', 'rose')
('jennie', 'rose', 'jisu', 'rose', 'jennie', 'lisa')
('jennie', 'rose', 'jisu', 'rose', 'jennie', 'rose')
('jennie', 'rose', 'jennie', 'lisa', 'jisu', 'lisa')
('jennie', 'rose', 'jennie', 'lisa', 'jisu', 'rose')
('jennie', 'rose', 'jennie', 'lisa', 'jennie', 'lisa')
('jennie', 'rose', 'jennie', 'lisa', 'jennie', 'rose')
('jennie', 'rose', 'jennie', 'rose', 'jisu', 'lisa')
('jennie', 'rose', 'jennie', 'rose', 'jisu', 'rose')
('jennie', 'rose', 'jennie', 'rose', 'jennie', 'lisa')
('jennie', 'rose', 'jennie', 'rose', 'jennie', 'rose')
```
### 8.4 permutations()

- iterable에서 원소개수가 r개인 순열 뽑기 

```python
>>> from itertools import permutations
>>> for i in permutations(iter):
...    print(i)
...
('jisu', 'jennie', 'lisa', 'rose')
('jisu', 'jennie', 'rose', 'lisa')
('jisu', 'lisa', 'jennie', 'rose')
('jisu', 'lisa', 'rose', 'jennie')
('jisu', 'rose', 'jennie', 'lisa')
('jisu', 'rose', 'lisa', 'jennie')
('jennie', 'jisu', 'lisa', 'rose')
('jennie', 'jisu', 'rose', 'lisa')
('jennie', 'lisa', 'jisu', 'rose')
('jennie', 'lisa', 'rose', 'jisu')
('jennie', 'rose', 'jisu', 'lisa')
('jennie', 'rose', 'lisa', 'jisu')
('lisa', 'jisu', 'jennie', 'rose')
('lisa', 'jisu', 'rose', 'jennie')
('lisa', 'jennie', 'jisu', 'rose')
('lisa', 'jennie', 'rose', 'jisu')
('lisa', 'rose', 'jisu', 'jennie')
('lisa', 'rose', 'jennie', 'jisu')
('rose', 'jisu', 'jennie', 'lisa')
('rose', 'jisu', 'lisa', 'jennie')
('rose', 'jennie', 'jisu', 'lisa')
('rose', 'jennie', 'lisa', 'jisu')
('rose', 'lisa', 'jisu', 'jennie')
('rose', 'lisa', 'jennie', 'jisu')
```

- leetcode example 869. Reordered Power of 2
- https://leetcode.com/problems/reordered-power-of-2/

```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(n)))
```
### reference 

[seu11ee.tistory](https://seu11ee.tistory.com/5)  

[itertools — 효율적인 루핑을 위한 이터레이터를 만드는 함수](https://docs.python.org/ko/3.8/library/itertools.html)  





