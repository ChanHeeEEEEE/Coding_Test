def solution(n):
    x=1
    c=1
    while n>=x:
        x=x*c
        c+=1
    return c-2