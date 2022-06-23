<style>
    g { color : Green }
</style>

# <g>🔴HBM ( high-bandwidth memory )</g>

- AMD + SK 하이닉스가 ( 2008 ~ 2013 ) 개발 시작.  
- 고대역 메모리
- 2022.06.23 기준 메모리 칩 기술에 비해 훨씬 더 빠르고, 전기 소비량은 적고, 공간도 덜 차지. 
- 리소스 사용량이 많은 고성능 컴퓨팅(HPC)와 인공지능(AI) app에 주목을 받음.  

## <g> problem </g>


- 높은 가격과 열 관리 문제
- 때에 따라 application을 수정해야 한다. 


## <g> ITworld News </g>

### HBM 작동 방식
HBM은 미국 칩 제조 업체 AMD와 한국의 메모리 칩 공급업체 SK 하이닉스가 함께 개발했다. 두 기업은 2008년부터 개발을 시작해 2013년에 반도체 업계 표준 기구인 JEDEC 컨소시엄에 사양을 전달했다. 2016년에 HBM2 표준이 승인된 데 이어 지난 1월 HBM3이 공식 발표됐다. HBM 메모리 칩의 주 제조업체는 한국의 삼성과 SK 하이닉스, 그리고 마이크론 테크놀로지다.  

HBM은 중앙 처리 장치(CPU)와 그래픽 처리 장치(GPU)의 성능에 비해 뒤처지는 표준 랜덤 액세스 메모리(DRAM)의 성능과 전력 문제를 해결하기 위해 개발됐다. 초기 대응책은 DRAM 용량을 늘리고 마더보드에 RAM 슬롯이라고도 하는 듀얼 인라인 메모리 모듈(DIMM) 슬롯을 늘리는 것이었다.  

그러나 문제는 메모리 자체가 아니라 버스에 있었다. 표준 DRAM 버스의 비트 폭은 4~32다. AMD의 부사장이자 HBM 메모리 개발자 중 한 명인 조 매크리에 따르면 HBM 버스의 비트 폭은 이보다 최대 128배 더 넓은 1,024에 이른다. 자동차에 비유하면 1차선 도로와 16차선 도로 중 어느 도로에서 더 많은 차가 다닐 수 있을지 생각하면 된다.  

HBM 기술은 대역폭을 높이기 위해 버스의 폭을 넓히는 것 외에, 메모리 칩의 크기를 줄여 새로운 설계 형식으로 적층한다. HBM 칩은 원래 그래픽 더블 데이터 레이트(GDDR) 메모리를 대체하기 위해 개발됐다. HBM 칩의 크기는 GDDR 메모리에 비해 매우 작아서 1GB GDDR 메모리 칩의 점유 면적은 672 제곱밀리미터인데 비해 1GB HBM은 35평방밀리미터에 불과하다.  

HBM은 트랜지스터를 옆으로 펼치지 않고 최대 12개 레이어 높이로 적층하고 ‘실리콘 관통 전극(TSV)’이라는 기술로 연결한다. TSV는 마치 건물 내의 엘리베이터처럼 HBM 칩의 레이어 사이를 움직이는 방법으로 데이터 비트의 이동에 필요한 시간을 크게 줄인다. 기판에서 CPU와 GPU 바로 옆에 HBM을 배치하면 CPU/GPU와 메모리 간의 데이터 이동에 필요한 전력도 낮아진다. CPU와 HBM이 직접 통신하므로 DIMM 스틱이 불필요하다. 매크리는 “매우 좁고 매우 빠른 방식 대신 매우 넓고 매우 느린 방식을 택한 것이다”라고 말했다.   
 
### HBM을 사용하는 제품
엔비디아의 가속 컴퓨팅 제품 관리 부문 선임 디렉터인 파레시 카리아는 표준 DRAM은 HPC 용으로는 잘 맞지 않는다고 말했다. DDR 메모리의 성능은 HBM 메모리에 근접할 수 있지만 이를 위해서는 많은 DIMM이 필요하고 에너지 효율성이 떨어진다.  

HPC에 HBM을 처음 사용한 업체는 후지쯔다. HPC 작업용으로 설계된 ARM 기반 A64FX 프로세서와 함께 HBM을 사용한다. A64FX를 탑재한 후가쿠(Fugaku) 슈퍼컴퓨터는 2020년 등장한 시점부터 슈퍼컴퓨터 500 순위에서 1위를 기록했으며 현재까지 1위를 유지하고 있다.  

엔비디아는 출시 예정인 호퍼(Hopper) GPU에 HBM3을 사용하며, 그레이스(Grace) CPU에는 DDR의 변형인 LPDDR5X 기술을 사용한다. AMD는 인스팅트(Instinct) MI250X 가속기(GPU 기술 기반)에 HBM2E를 사용하며 인텔은 제온 서버 프로세서의 일부 사파이어 래피드(Sapphire Rapids) 세대와 기업용 폰테 베키오(Ponte Vecchio) GPU 가속기에 HBM을 사용할 계획이다.  
 
### 앞으로 주류 애플리케이션에도 HBM이 쓰일까
전통적으로 기술은 최첨단에서 시작해 주류로 차차 확산한다. 예를 들어 액체 냉각은 처음에는 CPU에서 최대한 성능을 끌어내려는 게이머 사이에서 주로 사용된 비주류 기술이었지만, 지금은 모든 서버 업체가 프로세서, 특히 AI 프로세서를 위한 액체 냉각 방식을 제공한다.   

HBM도 주류로 진입할 수 있을까? 매크리는 같은 용량에서 HBM과 DDR의 가격 차이를 2:1 정도로 예상했다. 즉, 1GB HBM의 비용은 1GB DDR5의 2배 이상이다. 만일 메모리에 그 정도의 프리미엄을 지불한다면 투자에 상응하는 효과를 원하게 된다. 매크리는 “TCO 공식에서 성능은 분모에 위치하고 모든 비용은 분자에 위치한다. 성능이 2배가 되면 TCO도 2배로 좋아진다. 따라서 TCO를 개선하기 위한 최선의 방법은 성능이다”라고 말했다(매크리는 간단한 설명을 위해 비용은 일정하다고 가정했다).   

퓨처럼 리서치(Futurum Research)의 대표 애널리스트인 다니엘 뉴먼은 두 가지 이유에서 HBM이 주류로 편입되지 않을 것으로 예상했다. 첫 번째 비용이다. 뉴먼은 “비싸면 주류 시장에서 폭넓게 사용되지 않을 것이고 출하 물량도 줄어들게 된다”라고 말했다.   

두 번째 문제는 발열이다. 이미 냉각이 필요한 CPU에 5개 이상의 메모리 칩이 더해져 같은 쿨러를 공유하게 된다. 뉴먼은 “이 말은 매우 작은 패키지에서 많은 전력을 사용하게 되고 이로 인해 열 문제가 발생한다는 것을 의미한다. HBM을 사용하는 모든 프로세서에는 극히 효율적인 열 관리 기능이 필요하다”라고 말했다. 결국 AI와 HPC에서 이와 같은 가속기를 사용하는 경우 가속기를 구매해 운영해 얻는 성과만큼 비용도 더 든다는 것이다.   
 
### HBM을 사용하려면 애플리케이션을 수정해야 할까
새로운제목 2 메모리 패러다임에서 떠오르는 그다음 질문은 HPC와 AI 앱이 HBM 메모리의 모든 능력을 자동으로 활용하는지 아니면 재설계가 필요한지다. 전문가들은 애플리케이션을 처음에 어떻게 만들었는지에 따라 답이 달라진다고 말한다.   

카리아는 “많은 경우 애플리케이션 개발자는 시스템 기능상의 제약을 우회한다. 따라서 경우에 따라 새로운 기능을 반영해 애플리케이션을 재설계하거나 업데이트해야 할 수 있다”라고 말했다. 매크리는 "애플리케이션의 성능이 메모리 대역폭에 의해 제한되는 경우 애플리케이션을 수정하지 않아도 성능이 향상된다"라고 말했다. 단, 메모리 지연에 의해 제한되는 경우에는 HBM과 비교 대상 메모리 간의 본질적인 지연 차이 이외의 속도 향상은 없다. 이와 같은 애플리케이션은 수정해서 지연 현상을 유발하는 종속성을 제거해야 한다.   

매크리에 따르면, 많은 애플리케이션을 동시에 사용하는 부하가 시스템에 가해지는 경우에는 애플리케이션 성능이 지연에 의해 제한되더라도 성능이 향상될 가능성이 높다. HBM의 부하 지연이 더 낮기 때문이다. 카리아 역시 앱이 어떻게 만들어졌는지에 따라 답이 달라진다고 봤다. 그는 "기존 앱이 메모리 또는 지연과 같은 다양한 제약을 우회하도록 만들어진 경우 개발자는 새로운 기능을 반영해 애플리케이션을 재설계하거나 업데이트해야 한다. 새로운 컴퓨팅 아키텍처가 등장할 때 흔히 일어나는 일이다"라고 말했다.  
 
### HBM을 사용하려면 CPU에서 GPU로 전환해야 할까
또 다른 문제는 프로세서 아키텍처다. 오브젝티브 애널리시스(Objective Analysis)의 대표 애널리스트 짐 핸디에 따르면, HBM은 단일 명령 다중 데이터(SIMD) 프로세서에서 사용되는데, SIMD는 일반적인 서버 프로세서와는 완전히 다르게 프로그램된다는 점을 강조했다. X86과 ARM은 SIMD가 아니지만 GPU는 SIMD다. 핸디는 “일반 프로세서에서 실행되는 모든 프로그램은 SIMD 아키텍처를 활용하도록 재구성하고 재컴파일해야 한다. HBM이 뭔가를 바꿔서 그런 것이 아니라 프로세서 유형의 문제다”라고 말했다.    
 
### HBM 기술은 계속 발전한다
현재 판매되는 HBM 버전은 HBM2E지만 JEDEC는 지난 1월 HBM3의 최종 사양을 공개했다. HBM3은 같은 전압에서 HBM2E에 비해 작동 온도가 낮다. 또한 HBM3은 HBM2에 비해 핀당 데이터 전송률이 두 배로, 최대 6.4Gb/s에 이르고 독립 채널의 수도 8개에서 16개로 두 배로 늘어난다. 그 외의 다른 여러 성능 향상이 적용된다.   

SK 하이닉스, 삼성, 마이크론 등 모든 주요 메모리 업체가 HBM3 제품을 개발하고 있으며, 엔비디아의 호퍼 GPU를 시작으로 올해 서서히 제품이 출시되기 시작할 것이다. 현재 시점에서 HBM 사용은 최고 성능 제품에 국한된다. 카리아는 “이 CPU(그레이스)의 설계에서 지향하는 워크로드가 있다. 예를 들어 엑셀이나 마이크로소프트 오피스가 아니라 데이터센터 애플리케이션 분야에서 빛을 발하도록 설계됐다”라고 말했다.   
editor@itworld.co.kr  

원문보기:
https://www.itworld.co.kr/news/241169#csidx486aa35842c55fab26fd6ecc8008e26 