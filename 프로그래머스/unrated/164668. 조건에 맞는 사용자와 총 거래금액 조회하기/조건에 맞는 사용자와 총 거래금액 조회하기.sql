# -- 코드를 입력하세요
# Select a.USER_ID, a.NICKNAME, sum(a.price) TOTAL_SALES
#     from(
#     SELECT 
#         *,
#         # B.WRITER_ID, U.NICKNAME, 
#         sum(B.price) TOTAL_SALES
#         from USED_GOODS_BOARD B join USED_GOODS_USER U
#         on B.WRITER_ID = U.USER_ID
#         # where B.price >=700000 and B.STATUS = "DONE"
#         group by B.WRITER_ID
#         having sum(B.price) >=700000 and B.STATUS = "DONE"
#     order by B.price)a
    
-- 코드를 입력하세요
# SELECT 
#     # *,
#     B.WRITER_ID, U.NICKNAME, 
#     sum(B.price) TOTAL_SALES
#     from USED_GOODS_BOARD B join USED_GOODS_USER U
#     on B.WRITER_ID = U.USER_ID
#     # where B.price >=700000 and B.STATUS = "DONE"
#     group by B.WRITER_ID
#     having sum(B.price) >=700000 and B.STATUS = "DONE"
# order by B.price

SELECT
    # *,
    U.USER_ID,
    U.NICKNAME
    ,
    SUM(B.price) AS TOTAL_SALES
    # ,price
FROM
    USED_GOODS_BOARD B
JOIN
    USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
WHERE
    B.STATUS = "DONE"
#     B.price >= 700000
GROUP BY
    B.WRITER_ID
HAVING
    SUM(B.price) >= 700000
ORDER BY
    TOTAL_SALES;
