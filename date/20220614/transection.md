# tansection 격리 수준
참고 site : https://nesoy.github.io/articles/2019-05/Database-Transaction-isolation

## Transection isolation Level list
1. READ UNCOMMITTED
2. READ COMMITTED 
3. REPEATABLE READ
4. SERIALIZABLE

## 1. READ UNCOMMITTED
![class-diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/hundong2/plantUML/master/umlfile/test1.puml)

### READ UNCOMMITTED?

변경 내용이 `COMMIT` 이나 `ROLLBACK`에 상관 없이 다른 트랜젝션에서 접근 가능. 
사용을 권장하지 않음. 

### problem
`DRITY READ` 현상 발생
트랜젝션이 작업이 완료가 되지 않았지만 다른 트렌젝션에서 볼 수 있게 되는 현상. 

## 2. READ COMMITTED
![class-diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/hundong2/plantUML/master/umlfile/readcommitted.puml)

### READ COMMITTED ?
RDB에서 대부분 기본적으로 사용되고 있는 격리 수준. 
`Dirty Read`  와 같은 현상은 발생 안함. 
실제 테이블 값이 아닌 Undo 영역에 백업 된 레코드에서 값을 가져온다. 

### WARNNING 

 트랜젝션이 Commit한 이후 끝나지 않은 트랜젝션이 다시
 테이블 값을 읽으면 값이 변경 됨. 
 `REAPEATABLE READ`의 정합성에 어긋난다. 
 입출금 처리 시에 주로 발생. 



