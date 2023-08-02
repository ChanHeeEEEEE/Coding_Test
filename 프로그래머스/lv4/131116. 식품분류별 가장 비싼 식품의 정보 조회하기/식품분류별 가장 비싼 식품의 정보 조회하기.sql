SELECT CATEGORY, price MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT 
where (CATEGORY,price) in 
    (select CATEGORY, max(price) from FOOD_PRODUCT
    group by CATEGORY
    having CATEGORY in ('과자','국','김치','식용유'))
order by MAX_PRICE desc