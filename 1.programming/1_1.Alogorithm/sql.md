# SQL Tip

## List

[0. reference](#0-reference)  
[1. TABLE ALL](#1-all-data-view-of-table)  
[2. DATA ORDERING](#2-data-ordering)  
[3. DATA FILTERING](#3-data-filtering)  
[4. DATA LIMIT](#4-data-limit)  
[5. COLUMN NAME INDICATE](#5-data-as)  
[6. COUNT](#6-data-count)  
[7. SELECT 여러개](#7-select)  
[8. HAVING](#8-having)  
[9. SET](#9-set)  
[10. NULL](#10-nullable-data-null)  
[11. CASE WHEN](#11-case-when)  






## command set

### 1. all data view of [TABLE]
  
```sql
SELECT * FROM [TABLE];
```

### 2. data ordering
  
```sql
SELECT * FROM [TABLE] ORDER BY [COLUMN NAME] ASC or DESC;
```

```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```

### 3. data filtering

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = "Sick";
```

### 4. data LIMIT

```sql
SELECT NAME 
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
```

### 5. DATA 'AS'

```sql
-- 코드를 입력하세요
SELECT MAX(DATETIME) as 시간
FROM ANIMAL_INS;
```

### 6. DATA COUNT
```sql
SELECT COUNT(ANIMAL_ID) 
FROM ANIMAL_INS;
```

### 7. SELECT 

```sql
-- 코드를 입력하세요
SELECT COUNT(NAME) as count
FROM
(
SELECT NAME
FROM ANIMAL_INS
WHERE NAME != "NULL"
GROUP BY NAME ) B;
```

### 8. HAVING 

```sql
-- 코드를 입력하세요
SELECT  NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(*)>1 AND NAME IS NOT NULL
ORDER BY NAME;
```

### 9. SET

```sql
SET @HOUR := -1;
SELECT(@HOUR := @HOUR+1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) as COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23
```

### 10. Nullable data (NULL)

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is null; -- or WHERE NAME is not null;
```

### 11. CASE WHEN

```sql
SELECT ANIMAL_TYPE, CASE WHEN NAME IS NULL THEN 'No name' ELSE NAME END AS 'NAME' , SEX_UPON_INTAKE
FROM ANIMAL_INS;
```




### 0. reference

[HAVING/GROUP BY](http://www.gurubee.net/lecture/1032)  

