-- 코드를 입력하세요
SELECT ANIMAL_TYPE,
Case when NAME is null 
    then "No name"
    else NAME
    end
    NAME
    ,SEX_UPON_INTAKE
from ANIMAL_INS 
order by ANIMAL_ID
