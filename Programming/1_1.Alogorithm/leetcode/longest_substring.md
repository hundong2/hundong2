# 3. Longest Substring Without Repeating Chracters

[Longest Substring without Repeating chracters](https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/)  


## Problem 

Given a string s, find the length of the longest substring without repeating characters.  

### Example 1:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## My Solution

```python
class Solution:
    def seek_str(self, s: str) -> int:
        
        count = 1
        first = s[0]
        for _ in range(1, len(s)):
            if s[_] in first:
                break
            else:
                first += s[_]
                count += 1
        return count
            
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        
        strlist = list(s)
        maxval = 0
        #first = strlist[0]
        for _ in range(len(s)):
            maxval = max(maxval, self.seek_str(s[_:]))
        return maxval
        
```

## Tip 

All previous implementations have no assumption on the charset of the string s.

If we know that the charset is rather small, we can mimic what a HashSet/HashMap does with a boolean/integer array as direct access table. Though the time complexity of query or insertion is still O(1)O(1), the constant factor is smaller in an array than in a HashMap/HashSet. Thus, we can achieve a shorter runtime by the replacement here.

Commonly used tables are:

int[26] for Letters 'a' - 'z' or 'A' - 'Z'
int[128] for ASCII
int[256] for Extended ASCII

### Solution 

#### python

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res
```

#### C++

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // we will store a senitel value of -1 to simulate 'null'/'None' in C++
        vector<int> chars(128, -1);

        int left = 0;
        int right = 0;

        int res = 0;
        while (right < s.length()) {
            char r = s[right];

            int index = chars[r];
            if (index != -1 and index >= left and index < right) {
                left = index + 1;
            }
            res = max(res, right - left + 1);

            chars[r] = right;
            right++;
        }
        return res;
    }
};
```
