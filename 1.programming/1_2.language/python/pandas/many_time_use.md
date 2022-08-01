# Useful tip for pandas

## 1. Index column value diff

```python 
data.ix[80, 'year'] = 2000 #1 
data.loc[data.index==80,'year']=2000 #2
```

### reference 

https://flowingtime.tistory.com/entry/Python-panda-%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84-%EC%9E%90%EC%A3%BC-%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94-%EA%B5%AC%EB%AC%B8