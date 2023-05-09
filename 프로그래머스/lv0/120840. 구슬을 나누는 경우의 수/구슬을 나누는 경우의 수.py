def solution(balls, share):
    k=1
    for i in range(share) :
        k=k*(balls-i)/(i+1)
    return k