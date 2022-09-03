# 967. Numbers With Same Consecutive Differences

## Medium 

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.  

## Example1  

```
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
```

## Example2

```
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

## Constraints

```
2 <= n <= 9
0 <= k <= 9
```

## Solution 1

Approach 1: DFS (Depth-First Search)
Intuition

If one is not familiar with the concepts of DFS and BFS, we have an Explore card called Queue & Stack where we cover the DFS traversal as well as the BFS traversal.

In this section, we will start from the DFS strategy, which arguably is more intuitive for this problem.

As we stated in the overview section, we could build a valid digit combination digit by digit or (node by node in terms of tree).

For a number consisting of N digits, we start from the highest digit and walk through to the lowest digit. At each step, we might have several candidates that are eligible to be explored.

With the DFS strategy, we prioritize the depth over the breadth, i.e. we pick one of the candidates and continue the exploration before moving on to the other candidates that are of the same level.

Algorithm

Intuitively we could implement the DFS algorithm with recursion. Here we define a recursive function DFS(N, num) (in Python) whose goal is to come up the combinations for the remaining N digits, starting from the current num. Note that, the signature of the function is slightly different in our Java implementation. Yet, the semantics of the function remains the same.

## Algorithm

Intuitively we could implement the DFS algorithm with recursion. Here we define a recursive function DFS(N, num) (in Python) whose goal is to come up the combinations for the remaining N digits, starting from the current num. Note that, the signature of the function is slightly different in our Java implementation. Yet, the semantics of the function remains the same.

For instance, in the previous examples, where N=3 and K=2, and there is a moment we would invoke DFS(1, 13) which is to add another digit to the existing number 13 so that the final number meets the requirements. If the DFS function works properly, we should have the numbers of 135 and 131 as results after the invocation.

We could implement the recursive function in the following steps:

As a base case, when N=0 i.e. no more remaining digits to complete, we could return the current num as the result.

Otherwise, there are still some remaining digits to be added to the current number, e.g. 13. There are two potential cases to explore, based on the last digit of the current number which we denote as tail_digit.

Adding the difference K to the last digit, i.e. tail_digit + K.

Deducting the difference K from the last digit, i.e. tail_digit - K.

If the result of either above case falls into the valid digit range (i.e. [0, 9][0,9]), we then continue the exploration by invoking the function itself.

Once we implement the DFS(N, num) function, we then simply call this function over the scope of [1, 9][1,9], i.e. the valid digits for the highest position.

Note: If we are asked to return numbers of a single digit (i.e. N=1), then regardless of K, all digits are valid, including zero. We treat this as a special case in the code, since in our implementation of DFS function, we will never return zero as the result.  



```python
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        if N == 1:
            return [i for i in range(10)]

        ans = []
        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)
```