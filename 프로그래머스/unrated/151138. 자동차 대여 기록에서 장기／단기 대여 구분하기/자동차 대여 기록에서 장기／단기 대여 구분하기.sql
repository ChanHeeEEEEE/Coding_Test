SELECT  history_id, car_id,
     DATE_FORMAT(start_date, "%Y-%m-%d") start_date ,
     DATE_FORMAT(end_date, "%Y-%m-%d") end_date,
case when datediff(end_date, start_date) >=29 then "장기 대여"
    when datediff(end_date, start_date) <29 then "단기 대여"
    # else "단기 대여"
    end RENT_TYPE 
    # ,end_date-start_date
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where START_DATE like "2022-09%"
order by history_id desc

# select end_date-start_date, end_date,start_date from CAR_RENTAL_COMPANY_RENTAL_HISTORY 