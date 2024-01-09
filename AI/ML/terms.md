# Terms list of Machine Learning 

## List

### Tensor(텐서)

- 데이터를 위한 컨테이너(Container)
- 숫자를 위한 컨테이너(Container)
- 임의의 차원 개수를 가지는 행렬의 일반화된 모습
- dimension(차원) = axis(축)

### Saclar(스칼라)

- 0차원 텐서, 0D tensor
- numpy에서는 float32 or float64 타입의 숫자가 스칼라 텐서( array scalar ) 이다. 
- ndim속성을 사용하면 넘파이 배열의 축개수를 확인 할 수 있다. 
- scalar의 축 개수는 0 ( ndim == 0) 
- 축 개수를 rank(랭크)라고도 부른다. 
#### example

```python
import numpy as np
x = np.array(12)
array(12)
x.ndim
0
```
