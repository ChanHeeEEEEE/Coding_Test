-- 코드를 입력하세요
SELECT 
    # *,
    year(O.SALES_DATE) YEAR, month(O.SALES_DATE) MONTH, U.GENDER,
    count(Distinct O.USER_ID) USERS
from USER_INFO U inner join ONLINE_SALE O
on U.USER_ID = O.USER_ID 
# where GENDER is not null
group by YEAR,MONTH,GENDER
having GENDER is not null
order by year,month,gender