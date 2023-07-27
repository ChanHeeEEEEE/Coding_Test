-- 코드를 입력하세요
SELECT B.BOOK_ID , A.AUTHOR_NAME, 
    date_format(B.PUBLISHED_DATE,"%Y-%m-%d") PUBLISHED_DATE
    from BOOK B join AUTHOR A 
        on B.AUTHOR_ID = A.AUTHOR_ID
where category = "경제"
order by published_date