def solution(n):
    answer = 0
    if n%6 ==0:
        answer=n//6
    else: 
        c=1
        while True:
            num= n *c
            c+=1
            if num%6==0:
                answer= num//6
                break
    return answer