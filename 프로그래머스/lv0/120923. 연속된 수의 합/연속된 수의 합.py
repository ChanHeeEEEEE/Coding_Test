def solution(num, total):
    answer = []
    if num%2==0:
        start=total//num-num//2+1
        for i in range(num):
            answer.append(start)
            start+=1
    else:
        start=total//num-num//2
        for i in range(num):
            answer.append(start)
            start+=1                
    return answer