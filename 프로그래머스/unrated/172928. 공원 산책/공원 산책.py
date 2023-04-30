def solution(park, routes):
    answer = []
    X=park
    for k in range(len(park)) :
        for r in range(len(park[0])) :
            if park[k][r]=="S" :
                K=[k,r]
                NK=[k,r]
    Y=[k,r]

    for i in routes :
        if i[0]=="E" :
            op=1
            n=1
        if i[0]=="W" :
            op=1
            n=-1
        if i[0]=="S" :
            op=0
            n=1
        if i[0]=="N" :
            op=0
            n=-1

        for j in range(int(i[2])) :
            NK[op]=K[op]+n
            NK[1-op]=K[1-op]
            if NK[op]<0 or NK[op]>Y[op] :
                K[op]=K[op]-n*j
                break
            elif park[NK[0]][NK[1]]=="X" : 
                K[op]=K[op]-n*j
                break
            K[op]=NK[op]


    answer=K

    return answer