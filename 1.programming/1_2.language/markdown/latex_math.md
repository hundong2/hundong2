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

$
알파: alpha\; \alpha \\
크사이: xi\;	\xi	\\
베타: beta\;	\beta \\	
오미크론: omicron\;	\omicron \\	
감마:	\;gamma\;\gamma	\\
파이:	\;pi\;\pi \\	
델타:	\;delta\;\delta \\    \\	
로 :	\;rho\;\rho	\\
엡실론:	\;epsilon\;\epsilon	\\
시그마:	\;sigma\;\sigma	\\
제타:	\;zeta\;\zeta	\\
타우:	\;tau	\;\tau	\\
에타:	\;eta	\;\eta	\\
입실론:	\;upsilon\;\upsilon\\	
세타:	\;theta\;\theta	\\
파이:	\;phi	\;\phi	\\
이오타:	\;iota\;\iota	\\
카이:	\;chi	\;\chi	\\
카파:	\;kappa\;\kappa	\\
오메가:	\;omega\;\omega	\\
람다:	\;lamba\;\lambda	\\
뉴: \;nu\;	\nu	\\
뮤: \;mu\;	\mu	\\
$

$
합동	    :\;\backslash equiv	\; \equiv	\\
근사	    :\;\backslash approx	\; \approx	\\
비례	    :\;\backslash propto	\; \propto	\\
같고 근사	:\; \backslash simeq	\;  \simeq	\\
닮음	    :\;sim	\; \sim	\\
같지 않음	:\; neq	\;  \neq\\	
작거나 같음	:\;  leq	\;   \leq \\	
크거나 같음	:\;  geq	\;   \geq	\\
매우작음	:\;  ll	\;   \ll	\\
매우 큼	    :\; gg	\;  \gg	\\
$

$
불릿	   : \backslash bullet	\; \bullet	\\
부정	    :\backslash neq	    \; \neq	\\
wedge	 :  \backslash wedge	\; \wedge	\\
vee	       :\backslash vee	    \;\vee	\\
논리합	   : \backslash  oplus	\; \oplus	\\
어떤	   : \backslash exists	\; \exists	\\
오른쪽 </br>화살표	\; \backslash rightarro :\rightarrow	    \\
왼쪽 <\br>화살표	\; \backslash leftarrow :\leftarrow	\\
왼쪽 <\br>큰화살표	\; \backslash Leftarrow :\Leftarrow	\\
오른쪽 <\br>큰화살표\; \backslash  Rightarr	:\Rightarrow	\\
양쪽 <\br>큰화살표	\; \backslash Leftright :\Leftrightarrow	\\
양쪽 <\br>화살표	\; \backslash leftarrow :\leftarrow	\\
모든	            \;\backslash forall	:\forall	
$

$
교집합 \;\backslash cap:	    \cap \\	
합집합 \;\backslash cup:	    \cup	\\
상위집합 \;\backslash supset:	 \supset \\	
진상위집합 \;\backslash susseteq:	  \supseteq \\	
하위집합 \;\backslash subset:	  \subset	\\
진하위집 \;\backslash subseteq:	  \subseteq	 \\
부분집합아님 \backslash not\backslash subset:\;	\not\subset \\	
공집합	       \backslash emptyset, \backslash varnothing :\; \emptyset, \varnothing \\	
원소	        \backslash in\;: \in	\\
원소아님	    \backslash notin:\;\notin \\	
$

$
hat	\;\backslash hat{x} : \hat{x} \\	
widehat \;\backslash widehat{x}:\;	\widehat{x}	\\
물결 \;\backslash tilde{x} :\;		\tilde{x}	\\
wide물결 \;\backslash widetilde{x} :\;	\widetilde{x} \\	
bar	\;\backslash bar\{x\}:\;\bar{x} \\
overline \;\backslash overline\{x\}:\;	\overline{x} \\	
check	\;\backslash check\{x\}:\;\check{x}	\\
acute	\;\backslash acute\{x\}:\; \acute{x}	\\
grave	\;\backslash grave\{x\}:\;\grave{x}	\\
dot	\;\backslash dot\{x\}:\; \dot{x}	\\
ddot	\;\backslash ddot\{x\}:\;\ddot{x}	\\
breve	\;\backslash breve\{x\}:\;\breve{x}	\\
vec	\;\backslash vec\{x\}:\;\vec{x}	\\
델,나블라	\;\backslash nabla:\; \nabla	\\
수직	\;\backslash perp:\; \perp	\\
평행	\;\backslash parallel:\; \parallel	\\
부분집합아님	\;\backslash not\backslash subset :\; \not\subset\\	
공집합	\;\backslash emptyset:\; \emptyset	\\
가운데 점	\;\backslash cdot:\; \cdot	\\
…	\;\backslash dots:\; \dots	\\
가운데 점들	\;\backslash cdots:\; \cdots	\\
세로점들	\;\backslash vdots:\; \vdots	\\
나누기	\;\backslash div:\;\div	\\
물결표	\;\backslash sim:\; \sim	\\
플마,마플	\;\backslash pm \backslash mp:\; \pm, \mp	\\
겹물결표	\;\backslash approx:\; \approx	\\
prime	\;\backslash prime:\; \prime	\\
무한대	\;\backslash infty:\; \infty	\\
적분	\;\backslash int:\; \int	\\
편미분	\;\backslash :\; \partial	\\
한칸띄어	\;\backslash ,:\; x \, y	\\
두칸	\;\backslash ;:\; x\;y	\\
네칸띄어	\;\backslash quad:\; x \quad y	\\
여덟칸띄어	\;\backslash qquad:\; x \qquad y\\	
$

## Reference 

[wiki](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:TeX_%EB%AC%B8%EB%B2%95)  

https://jjycjnmath.tistory.com/117  

https://jaime-note.tistory.com/343  

https://velog.io/@s00ny0ung/%EC%A1%B0%EA%B0%81%EB%AA%A8%EC%9D%8C-%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4Markdown  

https://velog.io/@d2h10s/LaTex-Markdown-%EC%88%98%EC%8B%9D-%EC%9E%91%EC%84%B1%EB%B2%95  
