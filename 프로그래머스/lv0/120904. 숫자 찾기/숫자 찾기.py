def solution(num, k):
    answer = 0
    num=list(str(num))
    for idx,i in enumerate(num):
        if int(i) == k:            
            answer=idx+1
            break
        else:
            answer=-1            
    return answer