# Trapping Rain Water ( leetcode 42 )
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.  

![Example image](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

## example

```bash
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

## Example2 

```bash
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constrains:

- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 105`

## explanation ( python3 )

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        sum = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:   
                sum += left_max - height[left]
                left += 1
            else:
                sum += right_max - height[right]
                right -= 1
        return sum 
```


