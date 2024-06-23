# 대칭키 (Symmetric key)

- 대칭키는 노출 되면 Risk가 크다.
- ![symmetric key](./symmetric.puml)  

# 비대칭키 (Asymmetric key algorithm)  

- 한쌍의 Pair key를 가짐. 
- A, B 쌍의 키를 가지고 
  - A 키로 암호화, B 키로 복호화 가능. 
  - B 키로 암호화, A 키로 복호화 가능.
  - A 키로 암호화, A 키로 복호화 불가능. 
  - B 키로 암호화, B 키로 복호화 불가능. 
- public key( 공개키 )/ private key( 개인키, 비밀키 )  => RSA 알고리즘 ( 수학적 방법으로 연산하여 연산이 오래걸림. )
- TLS의 경우 최초에 대칭키를 공유하기 위해 RSA 비대칭키를 사용.  
  - 이후 실제 통신을 할 때는 대칭키를 활용하여 암호화 진행. 

![TLS information](./TLSInfo.puml)  

## CA Certificate 

- A회사 -> 도메인, 공개키 -> CA 검토 
- CA (Finger Print)   
  - A 회사 공개키를 `SHA256`으로 해시 -> `지문`으로 등록
- CA (Digital Signing)
  - `지문`을 CA의 개인키로 암호화 -> 인증서 `서명` 등록
- CA 인증서 발급 


## reference site 

- https://cuziam.tistory.com/entry/TLSHTTPS%EC%9D%98-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC%EC%99%80-%EA%B3%BC%EC%A0%95
- https://babbab2.tistory.com/7  
