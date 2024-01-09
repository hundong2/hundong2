# input 
## normal input
```python
for _ in range(100000):
    n = int(input())
    print(n)
```
## high performance input 
```python
import sys
for _ in range(100000):
    n = int(sys.stdin.readline())
    print(n)
```