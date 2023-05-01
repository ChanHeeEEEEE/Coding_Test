def solution(numbers):
    i=0
    answer=[]
    while True:
        try:
            answer.append(numbers[i]*2)
            i+=1
        except:
            break
    return answer