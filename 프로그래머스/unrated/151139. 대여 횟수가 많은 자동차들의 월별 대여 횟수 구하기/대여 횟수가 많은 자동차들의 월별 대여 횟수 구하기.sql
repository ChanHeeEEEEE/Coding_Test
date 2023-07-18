-- 코드를 입력하세요
Select
    month(start_date) month,
    CAR_ID,
    count(HISTORY_ID) RECORDS
from 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where (START_DATE between "2022-08-01" and "2022-10-31")
    and CAR_ID in 
        (select CAR_ID
         from CAR_RENTAL_COMPANY_RENTAL_HISTORY
         where (START_DATE between "2022-08-01" and "2022-10-31")
        group by CAR_ID
        having count(*) >=5
        )
group by CAR_ID, month
order by MONTH ,CAR_ID desc
