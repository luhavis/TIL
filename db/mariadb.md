# 테이블 이름, 설명 조회

```sql
SELECT
    table_name, table_comment
FROM
    information_schema.tables
WHERE
    table_schema = '';
```


# 테이블 내 컬럼 조회 

```sql
SELECT
    table_name, column_name, column_comment
FROM
    information_schema.columns
WHERE
    table_schema = '';
```