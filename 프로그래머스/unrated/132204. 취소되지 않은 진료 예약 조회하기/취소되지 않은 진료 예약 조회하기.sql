# SELECT P.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD,D.DR_NAME, P.APNT_YMD,P.APNT_CNCL_YMD
#     from DOCTOR D join 
#     (SELECT A.APNT_NO, A.PT_NO, PA.PT_NAME,A.MDDR_ID, A.APNT_YMD,A.APNT_CNCL_YMD
#      from PATIENT PA join APPOINTMENT A 
#     on PA.PT_NO = A.PT_NO
#         where A.APNT_CNCL_YMD is null or A.APNT_CNCL_YMD >=' 2022-4-13'
#         )P 
#         on D.DR_ID=P.MDDR_ID
# where D.MCDP_CD = "CS"
# order by P.APNT_YMD


SELECT P.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD,D.DR_NAME, P.APNT_YMD
    # ,P.APNT_CNCL_YMD
    # , p.k
    from DOCTOR D join 
    (SELECT A.APNT_NO, A.PT_NO, PA.PT_NAME,A.MDDR_ID, A.APNT_YMD
     # , DATE_FORMAT(A.APNT_YMD,'%Y-%m-%d') k
     ,A.APNT_CNCL_YMD
     from PATIENT PA join APPOINTMENT A 
    on PA.PT_NO = A.PT_NO
        where 
     A.APNT_CNCL_YMD is null 
     and 
     DATE_FORMAT(A.APNT_YMD,'%Y-%m-%d') = '2022-04-13'
        )P 
        on D.DR_ID=P.MDDR_ID
where D.MCDP_CD = "CS"
order by P.APNT_YMD
