# HTTPS 인증 방식

## reference ( by ) 

[[Network] HTTPS의 동작방식](https://inuplace.tistory.com/1086)  
[cloud](https://www.cloudflare.com/ko-kr/learning/ssl/what-is-ssl/)  

참고
https://www.cloudflare.com/ko-kr/learning/ssl/what-is-ssl/
https://www.cloudflare.com/ko-kr/learning/ssl/what-happens-in-a-tls-handshake/

![image](https://blog.kakaocdn.net/dn/cUKT0g/btrtqNLH8hi/UKnJKvLotmyHxKKgCj9DNK/img.jpg)  

기존의 HTTP 방식은 전송중인 데이터를 가로채면 누구나 데이터를 읽을 수 있었습니다. 가령 고객이 특정 쇼핑몰에서 신용카드 정보를 작성하여 서버에 전송하면, 해당 내용이 전혀 암호화되지 않은 채로 인터넷을 돌아다니게 되는 것입니다.

 

HTTPS는 HTTP의 이런 보안적 문제를 해결한 프로토콜입니다. HTTP를 SSL(Secure Sockets Layer) 프로토콜 위에서 돌아가도록하여 클라이언트와 서버가 주고받는 텍스트를 암호화합니다. 즉, HTTPS는 HTTP 프로토콜 + SSL 프로토콜인 것입니다. HTTPS를 사용하면 통신 내용이 공격자에게 공격받는 것을 방지할 수도 있고, 클라이언트는 접속하려는 서버가 신뢰할 수 있는 서버인지 판단할 수도 있습니다.

 

SSL 프로토콜은 SSL 인증서를 사용해 작동합니다. SSL 인증서는 클라이언트와 서버간의 통신을 제 3자가 보증해주는 전자화된 문서입니다. 클라이언트가 서버에 접속하면 서버는 클라이언트에게 이 인증서 정보를 전달합니다. 클라이언트는 먼저 이 인증서의 정보가 신뢰할 수 있는지 확인하고나서야, 작업을 수행합니다.

 

좀 더 자세히 이야기해봅시다. SSL 인증서에는 서비스의 정보(인증서를 발급한 CA, 서비스의 도메인 등)와 서버의 공개키가 포함되어 있습니다. 이 내용은 앞서 말한 제 3자인 CA(Certificate Authority, 공개키를 저장해주는 신뢰성이 검증된 민간 기업)에 의해 암호화됩니다. 이 때 공개키 암호화기법이 사용되는데, 특이하게 CA의 비공개키로 암호화가 진행됩니다. 이는 브라우저가 보유한 검증된 CA 공개키에 의해 복호화가 가능합니다. (cf. 브라우저는 신뢰된 CA 기업의 공개키는 모두 보유하고 있습니다. 따라서 바로 복호화가 가능합니다.)

 

브라우저가 보유한 CA 기업의 공개키로 복호화가 가능하다는 것은 그 데이터가 공개키와 쌍을 이루는 비공개키를 통해 암호화되었음을 인증하는 것과 같습니다. 즉, 해당 데이터가 CA 기업으로부터 왔음이 증명된 것입니다. 그리고 여기서 데이터는 SSL 인증서였죠? 이제 클라이언트는 해당 인증서 내부에 존재하는 서버의 공개키가 CA기업의 보안성 검증이 완료된 것임을 확인했습니다.

이제는 이 사이트를 신뢰할 수 있으므로 해당 공개키를 활용해 서버와 소통하며 대칭키인 "세션키"를 생성하고 이를 활용해 통신을 진행합니다. 이것이 HTTPS의 전반적인 과정입니다! ("세션 키"에 대해서는 아래의 SSL/TLS Handshake에서 설명하겠습니다.)

cf. SSL vs TLS
사실 SSL은 TLS(Transport Layer Security)라는 또 다른 프로토콜의 이전 버전입니다. IETF가 업데이트를 개발하고 Netscape는 더 이상 참여하지 않게되면서 이름이 변경되었다고 합니다.

그래서 사실 TLS 암호화, TLS Handshake라고 부르는 것이 좀 더 바람직하지만, SSL의 인지도가 워낙 높기 때문에 그냥 SSL로 부르거나 TLS/SSL 암호화, TSL/SSL Handshake와 같은 방식으로 부릅니다.

```
TLS/SSH handshake 
```

![image](https://blog.kakaocdn.net/dn/oPsgS/btrtq8PPTkC/0B7CvMAozDM1U3hwPRmvs0/img.png)  

앞서 클라이언트가 서버에 접속하면 서버는 클라이언트에게 SSL 인증서 정보를 전달하고, 해당 인증서가 확인이 된 이후에 내부에 존재하는 공개키를 활용해 "세션키" 라는 것을 생성하고 이를 활용해 통신을 시작한다고 했습니다. 이렇게 SSL 프로토콜을 활용해 통신을 수립하는 과정을 SSL/TLS Handshake라고 합니다.

+) SSL/TLS Handshake의 정확한 단계는 사용되는 키 교환 알고리즘의 유형과 양측에서 지원한는 암호 제품군 유형에 따라 다릅니다. 하지만 대부분 RSA 키 교환 알고리즘을 사용하므로, 그를 기준으로 살펴보겠습니다!  

![image](https://blog.kakaocdn.net/dn/u7qsE/btrtlmWoJll/N1bRxks98PDfBRsQNZjN5K/img.png)  

- "client hello" :
클라이언트가 서버로 hello 메세지를 전송하면서 핸드셰이크를 시작합니다. 이 메세지에는 클라이언트가 지원하는 TLS(SSL) 버전, 지원되는 암호 제품군, 그리고 "client random"이라고 하는 무작위 바이트 문자열이 포함됩니다.  

- "server hello" : 
클라이언트 hello 메시지에 대한 응답으로 서버가 서버의 SSL 인증서, 서버에서 선택한 암호 제품군, 그리고 서버에서 생성한 또 다른 무작위 바이트 문자열인 "server random"를 포함하는 메시지를 전송합니다.

- Verify server certificate :
클라이언트가 서버의 SSL 인증서를 인증서 발행 기관(CA)을 통해 검증합니다. 이를 통해 서버가 인증서에 명시된 서버인지, 클라이언트가 상호작용 중인 서버가 실제 해당 도메인의 소유자인지를 확인합니다.  

- Client key exchange : 
확인이 완료되면 클라이언트는 "The premaster secret"라고 하는 무작위 바이트 문자열을 공개 키로 암호화하여 전송합니다. (클라이언트는 서버의 SSL 인증서에서 공개 키를 받습니다.)
Send client certificate : 만약 서버가 클라이언트의 인증서를 요구한다면 서버의 인증서와 같은 방식으로 암호화를 진행하여 함께 전송합니다.  

- Verify client certificate : 
서버가 클라이언트로부터 받은 The premaster secret을 개인키를 통해 해독합니다.

- Client "finished" : 
클라이언트가 "client random", "server random", "The premaster secret"를 이용해 대칭키로 활용할 "세션 키"를 생성합니다. 클라이언트가 세션 키로 암호화된 "finished" 메시지를 전송합니다.

- Server "finished" : 
서버가 "client random", "server random", "The premaster secret"를 이용해 대칭키로 활용할 "세션 키"를 생성합니다. 서버가 세션 키로 암호화된 "finished" 메시지를 전송합니다.

- Exchange messages : 
핸드셰이크가 완료되고, 세션 키를 이용해 메세지를 주고 받습니다.  


## HTTPS의 사용

- A라는 서버를 만드는 기업이 HTTPS를 적용하기 위해 공개키와 개인키를 만듭니다.
- 신뢰할 수 있는 CA 기업에 공개키 관리를 부탁하며 계약을 맺습니다.
- 계약이 완료된 CA 기업은 A 서버의 공개키, 해당 기업의 이름, 공개키 암호화 방법을 담은 인증서를 만들고 해당 인증서를 CA 기업의 개인키로 암호화해서 A 서버에게 제공합니다.
- A 서버는 직접적인 공개키가 아닌 암호화된 인증서를 보유하게 되었습니다.
- 클라이언트가 통신 요청을 보내면 앞선 SSL/TLS Handshake 과정을 수행하여 연결을 수립합니다.
- 클라이언트와 A 서버와 통신을 시작합니다.