SELECT 
    # *,
    I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES,I.ADDRESS,
    round(avg(REVIEW_SCORE),2) SCORE
from REST_INFO I join REST_REVIEW R
on I.REST_ID = R.REST_ID
where I.ADDRESS like "서울%"
group by I.REST_ID
order by SCORE desc, I.FAVORITES desc
