def solution(my_str, n):
    answer = []
    k=0
    m=n
    for i in range(len(my_str)):
        if i == len(my_str)-1:
            answer.append(my_str[k:i+1])
            break
        if i == n-1:
            answer.append(my_str[k:i+1])
            k=i+1
            n+=m
        
            
    return answer