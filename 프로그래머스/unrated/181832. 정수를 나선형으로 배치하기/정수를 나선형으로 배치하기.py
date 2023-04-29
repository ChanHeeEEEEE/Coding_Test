def solution(n):
    ans=[[0 for _ in range(n)] for _ in range(n)]
    step=0
    ans[0][0]=1
    i=0
    j=0
    ii=0
    jj=0
    for k in range(0,n*n-1):
        if step ==0:
            jj =j+1
            if jj>=n or ans[i][jj]!=0 : 
                step+=1
        if step == 1:
            ii= i+1
            if ii>=n or ans[ii][j]!=0:
                step+=1
            else:
                i=ii
        if step ==2:
            jj= j-1
            if jj<0 or ans[i][jj]!=0:
                step+=1               
            else:
                j=jj
        if step ==3:
            ii =i-1
            if ii<0 or ans[ii][j]!=0:
                step-=3
            else:
                i=ii
        if step ==0:
            jj = j+1
            if jj>=n or ans[i][jj]!=0 : 
                step+=1
            else:
                j=jj
        ans[i][j] = k+2
        print(ans[i][j])
    return ans