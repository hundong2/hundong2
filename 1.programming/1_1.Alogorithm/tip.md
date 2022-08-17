# programming TIP

## 01. string, list 중복 제거 ( 정렬 없이 그대로 )

- set만 사용하면 정렬 한 값이 output  

```python
def func_example(self, s: str):
    list_str = list(dict.fromkeys(list(s)))
    return list_str
```

