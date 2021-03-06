# Hyperparameter?

- 머신러닝에서 하이퍼파라미터를 알기 위해서는 파라미터라는 개념을 알아야 합니다. 컴퓨터 프로그래밍에서의 파라미터(Parameter)는 어떤 시스템이나 함수의 특정한 성질을 나타내는 변수를 뜻하며, 매개변수라고도 합니다. 함수에 특정 파라미터를 전달함으로써 출력되는 값이 달라지게 되는데, 원하는 값을 얻기 위해서는 알맞은 파라미터를 입력해 주어야 합니다.
- 많은 사람들이 머신러닝을 배울 때 파라미터와 하이퍼파라미터의 개념의 차이를 잘 인지하지 못하는 경우가 대다수인데, 명확히 다른 개념인 것을 알아야 합니다. 그렇다면 머신러닝에서 사용하는 파라미터와 하이퍼파라미터는 어떤 것이며, 어떤 차이를 가지고 있을까요?
 
1. 파라미터(Parameter)
머신러닝에서 사용되는 파라미터는 모델 파라미터라고도 하며, 모델에 적용할 하나 이상의 파라미터를 사용하여 새로운 샘플에 대한 예측을 하기 위해 사용됩니다. 즉, 머신러닝 훈련 모델에 의해 요구되는 변수라 할 수 있습니다.
 
## 파라미터의 특징

예측 모델은 새로운 샘플을 주어지면 무엇을 예측할지 결정할 수 있도록 파라미터를 필요로 한다.
머신러닝 훈련 모델의 성능은 파라미터에 의해 결정된다.
파라미터는 데이터로부터 추정 또는 학습된다.
파라미터는 개발자에 의해 수동으로 설정하지 않는다.(임의로 조정이 불가능하다)
학습된 모델의 일부로 저장된다.

## 모델 파라미터의 예

### 인공신경망의 가중치
SVM(Support Vector Machine)의 서포트 벡터
선형 회귀 또는 로지스틱 회귀에서의 결정계수

 
2. 하이퍼파라미터(Hyperparameter)
머신러닝에서 하이퍼파라미터는 최적의 훈련 모델을 구현하기 위해 모델에 설정하는 변수로 학습률(Learning Rate), 에포크 수(훈련 반복 횟수), 가중치 초기화 등을 결정할 수 있습니다. 또한 하이퍼파라미터 튜닝 기법을 적용하여 훈련 모델의 최적값들을 찾을 수 있습니다.
 
## 하이퍼파라미터의 특징

- 모델의 매개 변수를 추정하는 데 도움이 되는 프로세스에서 사용된다.
- 하이퍼파라미터는 개발자에 의해 수동으로 설정할 수 있다.(임의 조정 가능)
- 학습 알고리즘의 샘플에 대한 일반화를 위해 조절된다.

## 하이퍼파라미터의 예

학습률  
손실 함수  
일반화 파라미터  
미니배치 크기  
에포크 수  
가중치 초기화  
은닉층의 개수  
k-NN의 k값  

## 하이퍼파라미터의 튜닝 기법

그리드 탐색  
랜덤 탐색  
베이지안 최적화  
휴리스틱 탐색  

 
## 정리

- 모델 파라미터는 새로운 샘플이 주어지면 무엇을 예측할지 결정하기 위해 사용하는 것이며 학습 모델에 의해 결정
- 하이퍼파라미터는 학습 알고리즘 자체의 파라미터로 모델이 새로운 샘플에 잘 일반화 되도록 하이퍼파라미터들의 최적값을 찾으나, 데이터 분석 결과로 얻어지는 값이 아니므로 절대적인 최적값은 존재하지 않고, 사용자가 직접 설정

출처: [IT is True:티스토리](https://ittrue.tistory.com/42)