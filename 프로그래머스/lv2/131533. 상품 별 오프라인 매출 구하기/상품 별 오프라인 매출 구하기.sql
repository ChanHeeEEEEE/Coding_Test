-- 코드를 입력하세요
SELECT P.product_code, sum(P.PRICE*O.SALES_AMOUNT) SALES 
from PRODUCT P join OFFLINE_SALE O
on P.PRODUCT_ID = O.PRODUCT_ID
group by product_code
order by SALES desc , product_code
