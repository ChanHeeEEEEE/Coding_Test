def solution(s):
    t=s.split()
    x=0
    y=len(t)-1
    while y>=0 :
        if t[y]=="Z" :
            y-=2
            continue
        x+=int(t[y])
        y-=1
    return x