def solution(age):
    n = list(map(str,str(age)))
    k=""
    for i in n:
        k+=chr(ord(i)+49)
    return k