# programming TIP

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

