-- 코드를 입력하세요
# SELECT 
#     # *,
#     CAR_ID,
#     case when (start_date <= "2022-10-16") and (end_date > "2022-10-17") then "대여중"
#     else "대여가능"
#     end AVAILABILITY 
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# group by CAR_ID
# order by CAR_ID desc

# select 
#     # *,
#     CAR_ID,
#     case when sum(cnt) !=0 then "대여중"
#     else "대여가능"
#     end AVAILABILITY
# from(
#     SELECT 
#         *,
#         case when 
#     (start_date <= "2022-10-16") and 
#     (end_date >= "2022-10-16") then 1
#         else 0
#         end cnt 
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY )a
# group by car_id
# order by CAR_ID desc

# select car_id,
#     case when 
#         sum(case when START_DATE <='2022-10-16' and 
#            END_DATE >='2022-10-16' then 1 else 0 end) =0 
#     then '대여가능'
#     else '대여중'
#     end AVAILABILITY    
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# group by car_id
# order by car_id desc

-- 코드를 입력하세요
SELECT
CAR_ID,
CASE
    WHEN SUM(CASE WHEN START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16'                    THEN 1 ELSE 0 END) = 0 THEN '대여 가능' ELSE '대여중' 
        END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
    