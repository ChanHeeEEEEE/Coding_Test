# def solution(array, n):
#     a=[i-n for i in array]
#     a = list(map(lambda x: abs(x) ,a))
#     a.index(min(a))
#     # -2와 2일 경우
#     return array[a.index(min(a))]

def solution(array, n):
    a=[i-n for i in array]
    b=[abs(i-n) for i in array]
    near=min(b)
    c=[]
    for i in a:
        if abs(i)==near:
            c.append(i)
    if len(c)==1:
        return c[0]+n
    else:
        return min(c)+n