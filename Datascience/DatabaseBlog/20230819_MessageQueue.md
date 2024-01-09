# How to Choose a Message Queue? Kafka vs. RabbitMQ

## reference 

[How to Choose a Message Queue? Kafka vs. RabbitMQ](https://blog.bytebytego.com/p/how-to-choose-a-message-queue-kafka)  

## Article 

```
In the last issue, we discussed the benefits of using a message queue. Then we went through the history of message queue products. It seems that nowadays Kafka is the go-to product when we need to use a message queue in a project. However, it's not always the best choice when we consider specific requirements.
```

```
지난 호에서는 메시지 큐 사용의 이점에 대해 논의했습니다. 그런 다음 메시지 큐 제품의 역사를 살펴보았습니다. 요즘 Kafka는 프로젝트에서 메시지 대기열을 사용해야 할 때 가장 많이 사용하는 제품인 것 같습니다. 그러나 특정 요구 사항을 고려할 때 항상 최선의 선택은 아닙니다.
```

---

### Database-Backed Queue

```
Let’s use our Starbucks example again. The two most important requirements are:

Asynchronous processing so the cashier can take the next order without waiting.

Persistence so customers’ orders are not missed if there is a problem.

Message ordering doesn’t matter much here because the coffee makers often make batches of the same drink. Scalability is not as important either since queues are restricted to each Starbucks location.

The Starbucks queues can be implemented in a database table. The diagram below shows how it works:
```

```
스타벅스의 예를 다시 사용합시다. 가장 중요한 두 가지 요구 사항은 다음과 같습니다. 
계산원이 기다리지 않고 다음 주문을 받을 수 있도록 비동기식 처리. 
문제가 있는 경우 고객의 주문이 누락되지 않음

커피 메이커는 종종 같은 음료를 일괄적으로 만들기 때문에 여기에서는 메시지 주문이 그다지 중요하지 않습니다. 대기열이 각 스타벅스 위치로 제한되기 때문에 확장성도 그다지 중요하지 않습니다.

스타벅스 대기열은 데이터베이스 테이블에서 구현할 수 있습니다. 아래 다이어그램은 작동 방식을 보여줍니다.
```
![image1](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ec6440f-9fd5-40c2-b32f-36b3caaac3e7_1262x770.jpeg)  

```
When the cashier takes an order, a new order is created in the database-backed queue. 
The cashier can then take another order while the coffee maker picks up new orders in batches.

출납원이 주문을 받으면 데이터베이스 지원 대기열에 새 주문이 생성됩니다. 
계산원은 커피 메이커가 새로운 주문을 일괄적으로 픽업하는 동안 다른 주문을 받을 수 있습니다.
```

```
Once an order is complete, the coffee maker marks it done in the database. 
The customer then picks up their coffee at the counter.

주문이 완료되면 커피 메이커는 데이터베이스에 완료 표시를 합니다. 
그런 다음 고객은 카운터에서 커피를 가져옵니다.
```

```
A housekeeping job can run at the end of each day to delete complete orders 
(that is, those with the “DONE status).

정리 작업은 매일 종료 시 실행되어 완료된 주문을 삭제할 수 있습니다.
(즉, "DONE 상태"인 주문)
```

```
For Starbucks’ use case, a simple database queue meets the requirements without needing Kafka. 
An order table with CRUD (Create-Read-Update-Delete) operations works fine.

Starbucks의 사용 사례에서는 간단한 데이터베이스 대기열이 Kafka 없이도 요구 사항을 충족합니다. 
CRUD(Create-Read-Update-Delete) 작업이 포함된 주문 테이블이 제대로 작동합니다.
```

### Redis-Backed Queue

```
A database-backed message queue still requires development work to create the queue table and read/write from it. \
For a small startup on a budget that already uses Redis for caching, Redis can also serve as the message queue.

데이터베이스 지원 메시지 큐는 여전히 큐 테이블을 생성하고 여기에서 읽기/쓰기를 위한 개발 작업이 필요합니다. 
이미 Redis를 캐싱에 사용하는 예산이 적은 소규모 스타트업의 경우 Redis가 메시지 대기열 역할을 할 수도 있습니다.
```

```
There are 3 ways to use Redis as a message queue:

1. Pub/Sub

2. List

3. Stream

The diagram below shows how they work.
```

![image2](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9651c4f-a045-4dcd-aa95-f25d819e75eb_1514x1202.jpeg)  

```
Pub/Sub is convenient but has some delivery restrictions. The consumer subscribes to a key and receives the data when a producer publishes data to the same key. The restriction is that the data is delivered at most once. If a consumer was down and didn’t receive the published data, that data is lost. Also, the data is not persisted on disk. If Redis goes down, all Pub/Sub data is lost. Pub/Sub is suitable for metrics monitoring where some data loss is acceptable.

The List data structure in Redis can construct a FIFO (First-In-First-Out) queue. The consumer uses BLPOP to wait for messages in blocking mode, so a timeout should be applied. Consumers waiting on the same List form a consumer group where each message is consumed by only one consumer. As a Redis data structure, List can be persisted to disk.

Stream solves the restrictions of the above two methods. Consumers choose where to read messages from - “$” for new messages, “<id>” for a specific message id, or “0-0” for reading from the start.

In summary, database-backed and Redis-backed message queues are easy to maintain. If they can't satisfy our needs, dedicated message queue products are better. We'll compare two popular options next. 
```

```
Pub/Sub는 편리하지만 일부 전송 제한이 있습니다. 소비자는 키를 구독하고 생산자가 동일한 키에 데이터를 게시할 때 데이터를 받습니다. 제한 사항은 데이터가 최대 한 번 전달된다는 것입니다. 소비자가 다운되어 게시된 데이터를 받지 못한 경우 해당 데이터가 손실됩니다. 또한 데이터는 디스크에 유지되지 않습니다. Redis가 다운되면 모든 Pub/Sub 데이터가 손실됩니다. Pub/Sub는 일부 데이터 손실이 허용되는 메트릭 모니터링에 적합합니다.

Redis의 목록 데이터 구조는 FIFO(선입선출) 대기열을 구성할 수 있습니다. 소비자는 BLPOP을 사용하여 차단 모드에서 메시지를 기다리므로 시간 제한을 적용해야 합니다. 동일한 목록에서 대기하는 소비자는 각 메시지가 한 소비자만 소비하는 소비자 그룹을 형성합니다. Redis 데이터 구조로서 List는 디스크에 유지될 수 있습니다.

Stream은 위 두 가지 방식의 제약을 해결합니다. 소비자는 메시지를 읽을 위치를 선택합니다. 새 메시지의 경우 "$", 특정 메시지 ID의 경우 "<id>" 또는 처음부터 읽는 경우 "0-0"입니다.

요약하면 데이터베이스 지원 및 Redis 지원 메시지 대기열은 유지 관리가 쉽습니다. 우리의 요구를 만족시킬 수 없다면 전용 메시지 대기열 제품이 더 좋습니다. 다음에 두 가지 인기 있는 옵션을 비교할 것입니다.
```

### RabbitMQ vs. Kafka

```
For large companies that need reliable, scalable, and maintainable systems, evaluate message queue products on the following:

1. Functionality
2. Performance
3. Scalability
4. Ecosystem

The diagram below compares two typical message queue products: RabbitMQ and Kafka.
```

![image3](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d19e154-30ae-4d9d-87fb-c9a94d708f45_842x1762.jpeg)  


### How They Work
```
RabbitMQ works like a messaging middleware - it pushes messages to consumers then deletes them upon acknowledgment. This avoids message pileups which RabbitMQ sees as problematic.

Kafka was originally built for massive log processing. It retains messages until expiration and lets consumers pull messages at their own pace.

작동 방식
RabbitMQ는 메시징 미들웨어처럼 작동합니다. 
메시지를 소비자에게 푸시한 다음 확인 시 삭제합니다. 이것은 RabbitMQ가 문제가 있는 것으로 보는 메시지 누적을 방지합니다.

Kafka는 원래 대규모 로그 처리를 위해 만들어졌습니다. 만료될 때까지 메시지를 보관하고 소비자가 원하는 속도로 메시지를 가져올 수 있습니다.
```

### Languages and APIs

```
RabbitMQ is written in Erlang which makes modifying the core code challenging. However, it offers very rich client API and library support.

Kafka uses Scala and Java but also has client libraries and APIs for popular languages like Python, Ruby, and Node.js.


RabbitMQ는 핵심 코드 수정을 어렵게 만드는 Erlang으로 작성되었습니다. 그러나 매우 풍부한 클라이언트 API 및 라이브러리 지원을 제공합니다.

Kafka는 Scala 및 Java를 사용하지만 Python, Ruby 및 Node.js와 같은 널리 사용되는 언어에 대한 클라이언트 라이브러리 및 API도 있습니다.
```

### Performance and Scalability ( 성능 및 확장성 )

```
RabbitMQ handles tens of thousands of messages per second. Even on better hardware, throughput doesn’t go much higher.

Kafka can handle millions of messages per second with high scalability. 

RabbitMQ는 초당 수만 개의 메시지를 처리합니다. 더 나은 하드웨어에서도 처리량은 훨씬 더 높아지지 않습니다.

Kafka는 높은 확장성으로 초당 수백만 개의 메시지를 처리할 수 있습니다.
```
### Ecosystem

```
Many modern big data and streaming applications integrate Kafka by default. This makes it a natural fit for these use cases.
많은 최신 빅 데이터 및 스트리밍 애플리케이션은 기본적으로 Kafka를 통합합니다. 따라서 이러한 사용 사례에 자연스럽게 적합합니다.
```

### Message Queue Use Cases

```
Now that we’ve covered the features of different message queues, let’s look at some examples of how to choose the right product.
다양한 메시지 대기열의 기능을 살펴보았으므로 이제 올바른 제품을 선택하는 방법에 대한 몇 가지 예를 살펴보겠습니다.
```

### Log Processing and Analysis

```
For an eCommerce site with services like shopping cart, orders, and payments, we need to analyze logs to investigate customer orders. 

The diagram below shows a typical architecture uses the “ELK” stack:

장바구니, 주문 및 결제와 같은 서비스를 제공하는 전자 상거래 사이트의 경우 로그를 분석하여 고객 주문을 조사해야 합니다.

아래 다이어그램은 "ELK" 스택을 사용하는 일반적인 아키텍처를 보여줍니다.

```

```
ElasticSearch - indexes logs for full-text search
전체 텍스트 검색을 위해 로그를 인덱싱합니다.

LogStash - log collection agent
로그 수집 에이전트

Kibana - UI for search and visualizing logs
로그 검색 및 시각화를 위한 UI

Kafka - distributed message queue
분산 메시지 큐
```

![images](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce542372-221a-41fa-997e-0ecaa3bb800a_1488x764.jpeg)  

