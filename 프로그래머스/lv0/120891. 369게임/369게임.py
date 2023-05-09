def solution(order):
    return len([i for i in str(order) if int(i)!= 0 and int(i)%3==0])
