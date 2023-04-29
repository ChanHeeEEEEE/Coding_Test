dx=(0,1,0,-1)
dy=(1,0,-1,0)
def solution(n):
    pro=[[0]*n for i in range(n)]
    x,y=0,0
    loc=2
    d=0
    pro[0][0]=1
    while loc<=n*n:
        nx,ny=x+dx[d],y+dy[d]
        if not(0<=nx<n and 0<=ny<n) or pro[nx][ny] !=0:
            d=(d+1)%4
            continue
        x,y=nx,ny
        pro[x][y]=loc
        loc +=1
    return pro
