# Latex grammer

## math markdown

### sum 

```
$100+300=400$

or

$$
100+300=400
$$
```
$100+300=400$

### mul

```
$3 \times 3 = 9$
```

$3 \times 3 = 9$

### div 

```
$3 \div 3 = 1$
```

$3 \div 3 = 1$

## fraction (분수)

```
$\frac{1}{3}$
```

$\frac{1}{3}$

```
$^1/_3$
```
$^1/_3$

## 수학 공식 수식 번호 

```
\tag{1}
```

$$
\frac{d}{dx}(\ln\,x)\,=\,\frac{1}{x}\tag{1}
$$

## 괄호 

```
$(\frac{1}{3})$
or
$\left(\frac{1}{3}\right)$ ( auto arrange () )
```

$(\frac{1}{3})\\$
$\left(\frac{1}{3}\right)$

### 괄호 크기 

```
$$\Bigg( \bigg( \Big( \big( (\mu) \big) \Big) \bigg) \Bigg)$$
```

$$\Bigg( \bigg( \Big( \big( ( \mu ) \big) \Big) \bigg) \Bigg)$$

### 중괄호 

```
$\{1+2\}$
```

$\{1+2\}$

### 대괄호 

```
$[1+3]$
```
$[1+3]$

## power 제곱

```
$e^1=e$
```

## 아래 첨자 Indices 

```
$\sum{n}(x_1,x_2,...,x_n)$
```

$\sum(x_1,x_2,...,x_n)$


## 생략 표시 dots

```
$\dots$
or 
$\cdots$
or 
$\vdots$
or 
$\ddots$ ( for matrix )
```
dot: $\dots$, cdot: $\cdots$, vdot: $\vdots$, ddot : $\ddots$

## root 

```
$\sqrt{2^2}=2$
```

$\sqrt{2^2}=2$

## factorial

```
$$n! = 1 \times 2 \times 3 \times \ldots n$$
```
$$n! = 1 \times 2 \times 3 \times \ldots n$$

## product 

```
$$n! = \prod_{k=1}^n k$$
```

$$n! = \prod_{k=1}^n k$$

## Set 

### 합집합

```
$$\{large,small,big\} \cup \{just,look\} = \{large,small,big,just,look\}$$
```

$$\{large,small,big\} \cup \{just,look\} = \{large,small,big,just,look\}$$


### 교집합, 공집합
```
$$\{large,small,big\} \cap \{just,look\} = \emptyset$$
```
$$\{large,small,big\} \cup \{just,look\} = \emptyset$$
$$\{large,small,big\} - \{just,look\} = \emptyset$$

$\{large,small,big\}^c = \{just,look\}$

### 포함 관계 

```
$\{large,small,big\} \notin \{just,look\}$

$\{just\} \in \{just,look\}$
```

$\{large,small,big\} \notin \{just,look\}$

$\{just\} \in \{just,look\}$

### 삼각함수

```$$1 = \cos^2 \theta + \sin^2 \theta$$```  
$1 = \cos^2 \theta + \sin^2 \theta$

- pi `$\pi$, $\Pi$, $\phi$` -> $\pi$, $\Pi$, $\phi$

- theta `$\theta$` -> $\theta$

- 180 degree(도) `$\180^\circ` -> $180^\circ$

## limit 극한

```$$\lim_{x \to \infty} \exp(-x) = 0$$```  
$\lim_{x \to \infty} \exp(-x) = 0$

## Sigma ( total Sum )

```
$\sum_{n=1}^{100}(x_1,x_2,...,x_n)$
```

$$\sum_{n}$$

$$\sum_{n=1}^{100}(x_1,x_2,...,x_n)$$

## log 

```
$\log_{a}{b}$
```

$\log_{a}{b}$

## 미분 differential

$\frac{d}{dt}t^{2}=2t$

## 적분 integral 

```
$$\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x$$

$$\int\limits_a^b$$
```

$$\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x$$

$$\int\limits_a^b$$

## matrix 행렬

```

$$A_{n,m} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,m} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,m} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{n,1} & a_{n,2} & \cdots & a_{n,m}
 \end{pmatrix}$$
```

$$A_{n,m} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,m} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,m} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{n,1} & a_{n,2} & \cdots & a_{n,m}
 \end{pmatrix}$$

```
$$ 
\begin{bmatrix}
a & b \\\\
c & d
\end{bmatrix}
$$
```

$$ 
\begin{bmatrix}
a & b \\\\
c & d
\end{bmatrix}
$$


## vector, scalar

```
$$\overrightarrow{VECTOR}$$

$$\overline{SCALAR}$$
```

$$\overrightarrow{VECTOR}$$

$$\overline{SCALAR}$$

## Line ( don't )

## special 
| 한글    | 그리스 문자 | 영어   | LaTeX  | LaTex 수식 |
|---------|-------------|--------|--------|------------|
| 알파    | α           | alpha  | \alpha | $\alpha$ |
| 크사이  | ξ           | xi     | \xi    | $\xi$    |
| 베타    | β           | beta   | \beta  | $\beta$  |
| 오미크론 | ο        | omicron| \omicron      |  $\omicron$      |
| 감마    | γ           | gamma  | \gamma | $\gamma$ |
| 파이    | π           | pi     | \pi    | $\pi$    |
| 델타    | δ           | delta  | \delta | $\delta$ |
| 로     | ρ           | rho    | \rho   | $\rho$   |
| 엡실론  | ϵ           | epsilon| \epsilon | $\epsilon$ |
| 시그마  | σ           | sigma  | \sigma | $\sigma$ |
| 제타    | ζ           | zeta   | \zeta  | $\zeta$  |
| 타우    | τ           | tau    | \tau   | $\tau$   |
| 에타    | η           | eta    | \eta   | $\eta$   |
| 입실론  | υ           | upsilon| \upsilon | $\upsilon$ |
| 세타    | θ           | theta  | \theta | $\theta$ |
| 파이    | ϕ           | phi    | \phi   | $\phi$   |
| 이오타  | ι           | iota   | \iota  | $\iota$  |
| 카이    | χ           | chi    | \chi   | $\chi$   |
| 카파    | κ           | kappa  | \kappa | $\kappa$ |
| 오메가  | ω           | omega  | \omega | $\omega$ |
| 람다    | λ           | lambda | \lambda| $\lambda$|
| 뉴     | ν           | nu     | \nu    | $\nu$    |
| 뮤     | μ           | mu     | \mu    | $\mu$    |

| 항목       | 기호  | LaTeX       | LaTeX (no $$)   |
|------------|-------|-------------|-----------------|
| 합동       | ≡     | $\equiv$    | \equiv          |
| 근사       | ≈     | $\approx$   | \approx         |
| 비례       | ∝     | $\propto$   | \propto         |
| 같고 근사  | ≃     | $\simeq$    | \simeq          |
| 닮음       | ∼     | $\sim$      | \sim            |
| 같지 않음  | ≠     | $\neq$      | \neq            |
| 작거나 같음 | ≤     | $\leq$      | \leq            |
| 크거나 같음 | ≥     | $\geq$      | \geq            |
| 매우 작음  | ≪     | $\ll$       | \ll             |
| 매우 큼    | ≫     | $\gg$       | \gg             |

| 항목       | 기호  | LaTeX       | LaTeX (no $$)   |
|------------|-------|-------------|-----------------|
| 불릿       | ∙     | $\bullet$   | \bullet         |
| 부정       | ≠     | $\neq$      | \neq            |
| 논리곱     | ∧     | $\wedge$    | \wedge          |
| 논리합     | ∨     | $\vee$      | \vee            |
| 배타적논리합 | ⊕   | $\oplus$    | \oplus          |
| 어떤       | ∃     | $\exists$   | \exists         |
| 오른쪽 화살표  | → | $\rightarrow$ | \rightarrow    |
| 왼쪽 화살표    | ← | $\leftarrow$  | \leftarrow      |
| 왼쪽 큰 화살표 | ⇐ | $\Leftarrow$  | \Leftarrow      |
| 오른쪽 큰 화살표 | ⇒ | $\Rightarrow$ | \Rightarrow     |
| 양쪽 큰 화살표   | ⇔ | $\Leftrightarrow$ | \Leftrightarrow |
| 양쪽 화살표      | ↔ | $\leftrightarrow$ | \leftrightarrow |
| 모든       | ∀     | $\forall$   | \forall         |


| 항목        | 기호             | LaTeX              | LaTeX (no $$)      |
|-------------|------------------|--------------------|--------------------|
| 교집합      | ∩                | $\cap$             | \cap               |
| 합집합      | ∪                | $\cup$             | \cup               |
| 상위집합    | ⊃                | $\supset$          | \supset            |
| 진상위집합  | ⊇                | $\supseteq$        | \supseteq          |
| 하위집합    | ⊂                | $\subset$          | \subset            |
| 진하위집합  | ⊆                | $\subseteq$        | \subseteq          |
| 부분집합아님 |             | $\not\subset$      | \not\subset        |
| 공집합      | ∅, ∅             | $\emptyset, \varnothing$ | \emptyset, \varnothing |
| 원소        | ∈                | $\in$              | \in                |
| 원소아님    |               | $\notin$           | \notin             |

| 항목                | 기호       | LaTeX             | LaTeX (no $$)   |
|---------------------|------------|-------------------|-----------------|
| hat (x에 적용)       | x^         | $\hat{x}$        | \hat{x}         |
| widehat (x에 적용)   | x          | $\widehat{x}$    | \widehat{x}     |
| 물결 (x에 적용)      | x~         | $\tilde{x}$      | \tilde{x}       |
| widetilde (x에 적용) | x          | $\widetilde{x}$  | \widetilde{x}   |
| bar (x에 적용)       | xˉ         | $\bar{x}$        | \bar{x}         |
| overline (x에 적용)  | x          | $\overline{x}$   | \overline{x}    |
| check (x에 적용)     | xˇ         | $\check{x}$      | \check{x}       |
| acute (x에 적용)     | xˊ         | $\acute{x}$      | \acute{x}       |
| grave (x에 적용)     | xˋ         | $\grave{x}$      | \grave{x}       |
| dot (x에 적용)       | x˙         | $\dot{x}$        | \dot{x}         |
| ddot (x에 적용)      | x¨         | $\ddot{x}$       | \ddot{x}        |
| breve (x에 적용)     | x˘         | $\breve{x}$      | \breve{x}       |
| vec (x에 적용)       | x          | $\vec{x}$        | \vec{x}         |
| 나블라               | ∇          | $\nabla$         | \nabla          |
| 수직                 | ⊥          | $\perp$          | \perp           |
| 평행                 | ∥          | $\parallel$      | \parallel       |
| 부분집합아님       |  ⊂        | $\not\subset$    | \not\subset     |
| 공집합               | ∅          | $\emptyset$      | \emptyset       |
| 가운데점            | ⋅          | $\cdot$          | \cdot           |
| 물결표              | ∼          | $\sim$           | \sim            |
| 플마,마플           | ±,∓        | $\pm,\mp$        | \pm,\mp         |
| 겹물결표           | ≈          | $\approx$        | \approx         |
| prime               | ′          | $\prime$         | \prime          |
| 무한대              | ∞          | $\infty$         | \infty          |
| 적분                | ∫          | $\int$           | \int            |
| 편미분              | ∂          | $\partial$       | \partial        |
| 한칸 띄어          | :xy        | $x\:y$           | x y             |
| 두칸 띄어          | ;xy        | $x\;y$           | x y             |
| 네칸 띄어          | quad:xy    | $x\quad y$       | x y             |
| 여덟칸 띄어        | qquad:xy   | $x\qquad y$      | x y             |


## Reference 

[wiki](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:TeX_%EB%AC%B8%EB%B2%95)  

https://jjycjnmath.tistory.com/117  

https://jaime-note.tistory.com/343  

https://velog.io/@s00ny0ung/%EC%A1%B0%EA%B0%81%EB%AA%A8%EC%9D%8C-%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4Markdown  

https://velog.io/@d2h10s/LaTex-Markdown-%EC%88%98%EC%8B%9D-%EC%9E%91%EC%84%B1%EB%B2%95  
