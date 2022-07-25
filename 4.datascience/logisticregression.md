# Logistic Regression

- Linear model을 기반으로하는 Classification
- 분류하는 선을 regressor의 원리로 그린다. 

## parameter explannation

Solver : default value - liblinear (L1, L2 모두 지원 )
max_iter : 해를 찾는데 있어서 반복 횟수 제한.

## python example 

- train set : kaggle titanic data set   

```python
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

# 원본 데이터를 재로딩, 데이터 가공, 학습데이터/테스트 데이터 분할. 
titanic_df = pd.read_csv('train.csv')
y_titanic_df = titanic_df['Survived']
X_titanic_df= titanic_df.drop('Survived', axis=1)
X_titanic_df = transform_features(X_titanic_df)

X_train, X_test, y_train, y_test = train_test_split(X_titanic_df, y_titanic_df, \
                                                    test_size=0.20, random_state=11)

lr_clf = LogisticRegression(solver='liblinear')

lr_clf.fit(X_train , y_train)
pred = lr_clf.predict(X_test)
get_clf_eval(y_test , pred)
```

## reference 

https://m.blog.naver.com/gdpresent/221703566189  
