![imgage javascript](https://www.freecodecamp.org/news/content/images/2022/06/Purple-Minimal-We-Are-Hiring-Twitter-Post--1--1.gif)  

자바스크립트를 배운지 얼마 되지 않았다면 "비동기"라는 용어를 들어본 적이 있을 것입니다.  
이것은 JavaScript가 비동기식 언어이기 때문입니다. 
그러나 그것이 실제로 의미하는 바는 무엇입니까?

# Synchronous(동기) vs Asynchronous(비동기)

기본적으로 JavaScript는 동기식 단일 스레드 프로그래밍 언어입니다.  
즉, 명령어는 병렬로 실행할 수 없고 하나씩만 실행할 수 있습니다.  

```javascript
let a = 1;
let b = 2;
let sum = a + b;
console.log(sum);
```

위의 코드는 두 숫자를 더한 다음 그 합계를 브라우저 콘솔에 기록합니다.   
인터프리터는 완료될 때까지 이러한 명령을 순서대로 차례로 실행합니다.  

## 단점

- 데이터베이스에서 많은 양의 데이터를 가져와 인터페이스에 표시하고 싶을 때.   
- 인터프리터가 이 데이터를 가져오는 명령에 도달하면 데이터를 가져와 반환할 때까지 나머지 코드의 실행이 차단됩니다. 
- 여러 다른 지점에서 데이터를 가져올 때의 지연은 사용자가 원하는 흐름대로 되지 않습니다.  

> synchronous JavaScript의 문제는 asynchronous JavaScript를 도입하여 해결되었습니다.

JavaScript가 비동기식으로 실행될 때 이전에 본 것처럼 명령이 반드시 하나씩 실행되는 것은 아닙니다.
이 비동기 동작을 적절하게 구현하기 위해 개발자가 수년 동안 사용한 몇 가지 솔루션이 있습니다.   
각 솔루션은 이전 솔루션을 개선하여 코드가 복잡해지는 경우 코드를 더 최적화하고 이해하기 쉽게 만듭니다.  

JavaScript의 비동기 특성을 더 이해하기 위해 콜백 함수, 약속, 비동기 및 기다림을 살펴보겠습니다.

## JavaScript에서 콜백이란 무엇입니까?
콜백은 다른 함수 내부에 전달된 다음 해당 함수에서 호출되어 작업을 수행하는 함수입니다.  

```javascript
console.log('fired first');
console.log('fired second');

setTimeout(()=>{
    console.log('fired third');
},2000);

console.log('fired last');
```

위의 스니펫은 콘솔에 내용을 기록하는 작은 프로그램입니다. 그러나 여기에 새로운 것이 있습니다.  
인터프리터는 첫 번째 명령을 실행한 다음 두 번째 명령을 실행하지만 세 번째 명령은 건너뛰고 마지막 명령을 실행합니다.  
두 setTimeout개의 매개변수를 사용하는 JavaScript 함수입니다.  
첫 번째 매개변수는 또 다른 함수이고 두 번째 매개변수는 해당 함수가 실행되어야 하는 시간(밀리초)입니다. 이제 콜백 정의가 실행되는 것을 볼 수 있습니다.  
이 경우 내부 함수 setTimeout는 2초(2000밀리초) 후에 실행되어야 합니다. 다른 명령이 계속 실행되는 동안 브라우저의 일부 별도 부분에서 실행되기 위해 실행된다고 상상해보십시오. 2초 후에 함수의 결과가 반환됩니다.  
이것이 프로그램에서 위의 스니펫을 실행하면 다음과 같은 결과를 얻을 수 있는 이유입니다.  

```bash
fired first
fired second
fired last
fired third
```
setTimeout함수 가 결과를 반환 하기 전에 마지막 명령어가 기록된 것을 볼 수 있습니다. 이 방법을 사용하여 데이터베이스에서 데이터를 가져왔다고 가정해 보겠습니다. 사용자가 데이터베이스 호출이 결과를 반환하기를 기다리는 동안 실행 흐름은 중단되지 않습니다.

이 방법은 매우 효율적이었지만 특정 지점에서만 가능했습니다. 때때로 개발자는 코드에서 서로 다른 소스를 여러 번 호출해야 합니다. 이러한 호출을 수행하기 위해 콜백은 읽거나 유지하기가 매우 어려워질 때까지 중첩됩니다. 이것을 콜백 지옥 이라고 합니다.

이 문제를 해결하기 위해 약속이 도입되었습니다.

## JavaScript에서 약속이란 무엇입니까?
우리는 사람들이 항상 약속을 하는 것을 듣습니다. 당신에게 공짜로 돈을 보내주겠다고 약속한 그 사촌, 허락 없이 다시는 쿠키 항아리를 만지지 않겠다고 약속한 꼬마... 하지만 자바스크립트의 약속은 약간 다릅니다.   
우리의 맥락에서 약속은 하는 데 시간이 걸릴 것입니다.  
Promise의 두 가지 가능한 결과가 있습니다.

우리는 약속을 실행하고 해결하거나
라인을 따라 약간의 오류가 발생하고 약속이 거부되었습니다.
콜백 함수의 문제를 해결하기 위해 약속이 따랐습니다. Promise는 두 가지 기능을 매개변수로 받습니다. 즉, resolve그리고 reject. 해결은 성공이고 거부는 오류가 발생할 때를 위한 것임을 기억하십시오.

```javascript
const getData = (dataEndpoint) => {
   return new Promise ((resolve, reject) => {
     //some request to the endpoint;
     
     if(request is successful){
       //do something;
       resolve();
     }
     else if(there is an error){
       reject();
     }
   
   });
};
```

위의 코드는 일부 엔드포인트에 대한 요청으로 묶인 약속입니다. 
약속은 내가 ​​전에 언급한 것처럼 resolve받아 들입니다.reject

예를 들어 엔드포인트를 호출한 후 요청이 성공하면 약속을 해결하고 계속해서 응답으로 원하는 작업을 수행합니다. 그러나 오류가 있으면 약속이 거부됩니다.

Promise는 Promise Chaining 이라는 방법으로 콜백 지옥으로 인해 발생하는 문제를 해결하는 깔끔한 방법 입니다. 이 방법을 사용하여 여러 끝점에서 데이터를 순차적으로 가져올 수 있지만 더 적은 코드와 더 쉬운 방법을 사용합니다.  

하지만 더 좋은 방법이 있습니다! JavaScript에서 데이터 및 API 호출을 처리하는 데 선호되는 방법이므로 다음 방법에 익숙할 것입니다.  

## JavaScript에서 Async 및 Await는 무엇입니까?
문제는 콜백과 마찬가지로 약속을 함께 묶는 것이 부피가 크고 혼란스러울 수 있다는 것입니다. 이것이 Async와 Await가 탄생한 이유입니다.  

비동기 함수를 정의하려면 다음을 수행합니다.  

```javascript 
const asyncFunc = async() =>
{

}
```

비동기 함수를 호출하면 항상 Promise가 반환됩니다. 이것을 보십시오:

```javascript 
const test = asyncFunc();
console.log(test);
```
브라우저 콘솔에서 위를 실행하면 asyncFunc약속이 반환되는 것을 볼 수 있습니다.
이제 실제로 일부 코드를 분해해 보겠습니다. 

```javascript
const asyncFunc = async () => {
	const response = await fetch(resource);
   	const data = await response.json();
}
```

async키워드는 위에서 언급한 것처럼 비동기 함수를 정의하는 데 사용하는 것입니다 . 하지만 어떻 await습니까? fetch는 약속이 해결될 때까지 JavaScript가 응답 변수에 할당하는 것을 지연시킵니다. 약속이 해결되면 이제 fetch 메서드의 결과를 응답 변수에 할당할 수 있습니다.
3행에서도 같은 일이 발생합니다. 이 .json메서드는 약속을 반환하고 await여전히 약속이 해결될 때까지 할당을 지연하는 데 사용할 수 있습니다.

코드 차단 여부
내가 '정지'라고 말할 때 Async 및 Await를 구현하면 어떻게든 코드 실행이 차단된다고 생각해야 합니다. 요청이 너무 오래 걸리면 어떻게 합니까?

사실은 그렇지 않습니다. 비동기 함수 내부에 있는 코드가 차단되지만 프로그램 실행에는 영향을 미치지 않습니다. 우리 코드의 실행은 그 어느 때보 다 비동기식입니다. 이것을 보여주기 위해,  

```javascript
const asyncFunc = async () => {
	const response = await fetch(resource);
   	const data = await response.json();
}

console.log(1);
cosole.log(2);

asyncFunc().then(data => console.log(data));

console.log(3);
console.log(4);
```

브라우저 콘솔에서 위의 출력은 다음과 같습니다.  

```bash
1
2
3
4
data returned by asyncFunc
```

를 호출 asyncFunc했을 때 함수가 결과를 반환할 때까지 코드가 계속 실행되었음을 알 수 있습니다.

## 결론
이 기사에서는 이러한 개념을 깊이 있게 다루지 않지만 비동기 JavaScript가 수반하는 것과 주의해야 할 몇 가지 사항을 보여주기를 바랍니다.
이것은 JavaScript의 매우 필수적인 부분이며 이 기사는 표면만 긁는 것입니다. 그럼에도 불구하고 이 기사가 이러한 개념을 무너뜨리는 데 도움이 되었기를 바랍니다.  


## reference 

[freecodecamp](https://www.freecodecamp.org/news/asynchronous-javascript-explained/)  
