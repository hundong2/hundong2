# Build Error 

# *** non-numeric second argument to 'wordlist' function: 'std5wAndroid'.  Stop.

## 01. Error Message 

```sh
android-ndk-r12b/build/gmsl/__gmsl:512: *** non-numeric second argument to 'wordlist' function: 'std5wAndroid'.  Stop.
```

## 02. Solution

- OS의 특수문자의 차이로 발생하는 문제. 


```sh
#int_encode = $(__gmsl_tr1)$(wordlist 1,$1,$(__gmsl_input_int))
int_encode = $(__gmsl_tr1)$(wordlist 1,$(words $1),$(__gmsl_input_int))
```

## 03. reference 
[Stackoverflow](https://stackoverflow.com/questions/17131691/non-numeric-second-argument-to-wordlist)   