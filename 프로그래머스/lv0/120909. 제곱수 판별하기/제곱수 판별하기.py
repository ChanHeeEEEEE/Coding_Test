def solution(n):
    return 1 if len([i for i in range(1,n+1) if i*i == n]) == 1 else 2