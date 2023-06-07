def solution(A, B):
    answer = 0
    temp=[]
    A=list(A)
    B=list(B)
    for i in range(len(A)):
        if A==B:
            break
        a=A[-1]
        A = A[:-1]
        A.insert(0,a)
        answer+=1
    if answer==len(A):
        answer=-1
    return answer