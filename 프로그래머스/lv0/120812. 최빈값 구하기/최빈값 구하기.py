def solution(array):
    answer=0
    a=list(set(array))
    b=[]
    for i in a:
        b.append(array.count(i))
    c=0
    for j in b:
        if j == max(b):
            c+=1
    
    if c!=1:
        answer= -1
    else:
        answer=a[b.index(max(b))]

    
    return answer 