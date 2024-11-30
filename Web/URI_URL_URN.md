# URL, URI, URN의 정의와 차이점

## URI (Uniform Resource Identifier)
URI는 인터넷 리소스를 식별하는 문자열입니다. URI는 두 가지 주요 하위 집합인 URL과 URN을 포함합니다. URI는 리소스를 고유하게 식별할 수 있는 방법을 제공합니다.

## URL (Uniform Resource Locator)
URL은 인터넷 상의 리소스의 위치를 지정하는 문자열입니다. URL은 리소스에 접근하기 위한 프로토콜(예: HTTP, HTTPS, FTP)과 리소스의 위치를 포함합니다. 예를 들어, `https://www.example.com/index.html`은 웹 페이지의 URL입니다.

## URN (Uniform Resource Name)
URN은 리소스를 고유하게 식별하는 이름입니다. URN은 리소스의 위치와는 무관하게 리소스를 식별할 수 있습니다. 예를 들어, `urn:isbn:0451450523`은 특정 책의 ISBN을 나타내는 URN입니다.

## 차이점
- **URI**: 인터넷 리소스를 식별하는 모든 문자열을 포함합니다.
- **URL**: 리소스의 위치를 지정하는 URI의 하위 집합입니다.
- **URN**: 리소스를 고유하게 식별하는 이름으로, 위치와는 무관합니다.

## 구조도
```
URI
├── URL
│   ├── http://www.example.com
│   ├── https://www.example.com
│   └── ftp://ftp.example.com
└── URN
    ├── urn:isbn:0451450523
    └── urn:ietf:rfc:2141
```

## 예시
- **URI**: `https://www.example.com/index.html`, `urn:isbn:0451450523`
- **URL**: `https://www.example.com/index.html`
- **URN**: `urn:isbn:0451450523`

## 참고 RFC
- [RFC 1738: Uniform Resource Locator(URL)](https://datatracker.ietf.org/doc/html/rfc1738)  
- [RFC 3986: Uniform Resource Identifier (URI): Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)
- [RFC 2141: URN Syntax](https://datatracker.ietf.org/doc/html/rfc2141)