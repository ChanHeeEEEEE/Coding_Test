def solution(array):
    answer = [] 
    answer.append(max(array))
    for i in range(len(array)):
        if array[i] == max(array):
            answer.append(i)
            
    # answer.append(max(array).index())
    return answer