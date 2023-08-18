# select cart_id
# from CART_PRODUCTS
# group by cart_id
# having group_concat(name) like '%Milk%' and group_concat(name) like '%Yogurt%'
# order by 1

SELECT DISTINCT A.CART_ID
FROM CART_PRODUCTS A 
INNER JOIN CART_PRODUCTS B ON A.CART_ID = B.CART_ID
WHERE A.NAME LIKE 'Yogurt' AND B.NAME LIKE 'Milk'
ORDER BY A.CART_ID


# select cart_id
# from (select cart_id, name
#      from cart_products
#      where name in ('Yogurt', 'Milk')
#      group by cart_id,name)
#      a
# group by cart_id
# having count(cart_id)>=2
# order by cart_id;


# select cart_id
# from (
#     select distinct cart_id
#         , NAME
#     from CART_PRODUCTS
#     where name in ('Milk','Yogurt')) tbl
# group by 1
# having count(cart_id) >= 2
# order by 1