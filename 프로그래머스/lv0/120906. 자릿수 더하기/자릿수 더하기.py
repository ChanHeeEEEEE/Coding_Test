def solution(n):
    answer = 0
    n=str(n)
    n=list(n)
    n=list(map(int,n))
    for i in n:
        answer+=i
        
    return answer