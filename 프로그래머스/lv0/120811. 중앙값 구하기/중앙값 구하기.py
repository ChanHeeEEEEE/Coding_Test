def solution(array):
    array.sort()
    n=len(array)
    if n %2 == 0:
        answer =array[n/2-1]/2+array[n/2]/2 
    else:
        answer = array[int((n-1)/2)]
        #answer = array[(n//2)]
        
    
    return answer