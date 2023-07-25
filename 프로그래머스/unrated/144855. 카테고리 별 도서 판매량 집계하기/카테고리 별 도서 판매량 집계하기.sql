-- 코드를 입력하세요
# SELECT 
# B.CATEGORY , sum(S.TOTAL_SALES) TOTAL_SALES
# from (select book_id, sales_date, sum(sales) TOTAL_SALES 
#       from BOOK_SALES group by book_id) S 
# join BOOK B  
# on B.BOOK_ID = S.BOOK_ID
# WHERE S.SALES_DATE between '2022-01-01' and '2022-01-31'
# group by B.CATEGORY
# order by CATEGORY

SELECT
    B.CATEGORY,
    SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B
    JOIN BOOK_SALES S
    ON B.BOOK_ID = S.BOOK_ID
        WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY;
