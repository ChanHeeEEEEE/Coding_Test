SELECT 
    # *,
    P.PRODUCT_ID,P.PRODUCT_NAME, 
    # sum(P.PRICE),sum(O.AMOUNT),
    # P.PRICE*O.AMOUNT TOTAL_SALES
    P.PRICE*sum(O.AMOUNT) TOTAL_SALES
from FOOD_PRODUCT P join FOOD_ORDER O 
on P.PRODUCT_ID = O.PRODUCT_ID
where PRODUCE_DATE like "2022-05%"
group by p.PRODUCT_ID
order by TOTAL_SALES desc, P.PRODUCT_ID 
