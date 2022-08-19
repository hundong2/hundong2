# programming TIP

- [programming TIP](#programming-tip)
  - [01. string, list 중복 제거 ( 정렬 없이 그대로 )](#01-string-list-중복-제거--정렬-없이-그대로-)
  - [02. array 2차원 초기화](#02-array-2차원-초기화)
    - [leetcode example 2373. Largest Local Values in a Matrix](#leetcode-example-2373-largest-local-values-in-a-matrix)
  - [03. dictionary value 값에 따라 sort](#03-dictionary-value-값에-따라-sort)
  - [04. for loop](#04-for-loop)
    - [4.1 for range](#41-for-range)
    - [4.2 for reversed range](#42-for-reversed-range)
  - [05. List](#05-list)
    - [5.1 List strint to integer convert](#51-list-strint-to-integer-convert)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
 

<style type="text/css">
    ol { list-style-type: upper-alpha; }
</style>

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


