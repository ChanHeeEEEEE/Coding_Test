def solution(numer1, denom1, numer2, denom2):
    mother=denom1*denom2
    son=numer1*denom2+numer2*denom1
    for i in range(1,1001*1001):
        if mother%i==0 and son%i==0:
            m=int(mother/i)
            s=int(son/i)

    answer=[s,m]
    return answer