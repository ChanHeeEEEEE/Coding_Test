#이게 뭐지?
def solution(n):
    c=0
    for i in range(1,n+1):
        if len([j for j in range(1,i+1) if i%j==0]) >=3:
            c+=1
    return c