select B.FLAVOR from (
    SELECT A.FLAVOR, A.FTO + A.JTO FJTO
    from (
        SELECT J.FLAVOR ,sum(F.TOTAL_ORDER) FTO, sum(J.TOTAL_ORDER) JTO
            from FIRST_HALF F
            right join JULY J
            on F.SHIPMENT_ID = j.SHIPMENT_ID
        group by J.FLAVOR
        ) A
    order by FJTO desc
    limit 3) B
