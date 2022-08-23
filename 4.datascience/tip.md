# Tip of datasicence tool ( python )  

- [Tip of datasicence tool ( python )](#tip-of-datasicence-tool--python-)
  - [1. numpy](#1-numpy)
    - [1.1 tensor](#11-tensor)
      - [input](#input)
      - [output](#output)
      - [ndim ( 차원 표시 )](#ndim--차원-표시-)
    - [1.2 export_graphviz](#12-export_graphviz)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1. numpy   

### 1.1 tensor

#### input

```python
import numpy as np

array1 = np.array([1,2,3]) # 1 차원 array 
print('array1 type:',type(array1))
print('array1 array 형태:',array1.shape)

array2 = np.array([[1,2,3],
                  [2,3,4]])
print('array2 type:',type(array2))
print('array2 array 형태:',array2.shape)

array3 = np.array([[1,2,3]])
print('array3 type:',type(array3))
print('array3 array 형태:',array3.shape)
``` 

#### output   

```bash
array1 type: <class 'numpy.ndarray'>
array1 array 형태: (3,)
array2 type: <class 'numpy.ndarray'>
array2 array 형태: (2, 3)
array3 type: <class 'numpy.ndarray'>
array3 array 형태: (1, 3)
```

#### ndim ( 차원 표시 )  

```python
print('array1: {:0}차원, array2: {:1}차원, array3: {:2}차원'.format(array1.ndim,array2.ndim,array3.ndim))
#array1: 1차원, array2: 2차원, array3:  2차원
```

### 1.2 export_graphviz 

[explanation](../4.datascience/library/sklearn_tree.md#exportgraphviz)  
  
```python
from sklearn.tree import export_graphviz
```

