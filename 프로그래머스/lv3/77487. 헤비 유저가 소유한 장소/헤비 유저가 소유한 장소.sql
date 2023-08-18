# -- 코드를 입력하세요
# SELECT * from PLACES
#     where () >=2
# order by HOST_ID


SELECT * from PLACES
    where HOST_ID in (select HOST_ID from (select HOST_ID ,count(HOST_ID) cnt
    from PLACES
    group by HOST_ID
    having cnt >=2)a)
order by ID
