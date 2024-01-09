# 1. weak_ordering 

- '<=>' 우주선 연산 시 모든 개체가 같지 않고, 동등한 관계일 경우 

```
less
greater
equivalent
```

# 2. strong_ordering

```
less
greater
equal
equivalent
```

# 3. partial_ordering

```
less
greater
equivalent
unordered
```

```c++
auto ret2 = (3.4 <=> 2.1); // NaN => Not A Number
```