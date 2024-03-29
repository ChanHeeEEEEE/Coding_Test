# SELECT 
#     FOOD_TYPE,REST_ID,REST_NAME,FAVORITES 
# from REST_INFO 
# where FAVORITES in (select max(FAVORITES) from REST_INFO group by FOOD_TYPE)
# group by FOOD_TYPE
# having FAVORITES = max(FAVORITES)
# order by FOOD_TYPE desc

Select FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
from REST_INFO R1
group by FOOD_TYPE,FAVORITES
having FAVORITES =  
    (select max(FAVORITES) from REST_INFO R2
    where R1.FOOD_TYPE = R2.FOOD_TYPE)
order by FOOD_TYPE desc

# SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
# FROM REST_INFO AS R1
# GROUP BY FOOD_TYPE, FAVORITES
# HAVING FAVORITES = (
#   SELECT MAX(FAVORITES)
#   FROM REST_INFO AS R2
#   WHERE R2.FOOD_TYPE = R1.FOOD_TYPE

#     # R1 : REST_INFO에서 (FOOD_TYPE,FAVORITES) 로 그룹화 된 상태
#     # R2 : REST_INFO 본연의 상태

#     # 서브쿼리의 진행 과정은 다음과 같다.

#     # 'WHERE R2.FOOD_TYPE = R1.FOOD_TYPE': 현재 R1에서의 튜플이 가진 FOOD_TYPE이 R2에서 FOOD_TYPE 과 일치하는 R2 튜플을 모은다. (R1과 R2의 모든 튜플을 FOOD_TYPE 기준으로 한번에 이어붙이는 형태가 아니다)

#     # SELECT MAX(FAVORITES) : 그 튜플들의 MAX(FAVORITES)을 계산하고, 

#     # HAVING FAVORITES = (...) : HAVING절을 통해 이 그룹에서 그 값과 같은 것만 남긴다.(조건문역할)
# )
# ORDER BY FOOD_TYPE DESC;