# 238. Product of Array Except Self ( leetcode )

Given an integer array `nums`, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].  
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

 

## Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

## Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

## Constraints:

```
2 <= nums.length <= 105
-30 <= nums[i] <= 30
```

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.  

## explanation

```python
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = math.prod(nums)
        mul2 = 0
        zerocount = nums.count(0)
        if  zerocount > 1:
            mul2 = 0
        elif zerocount == 1:
            mul2 = math.prod(nums[:nums.index(0)]) * math.prod(nums[nums.index(0)+1:])

        a = [int(mul / _) if _ != 0 else mul2 for _ in nums ]
            
        return a
```