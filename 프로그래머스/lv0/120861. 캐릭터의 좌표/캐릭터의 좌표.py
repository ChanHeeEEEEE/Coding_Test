def solution(keyinput, board):
    a = [0,0]
    x=(board[0]-1)/2
    y=(board[1]-1)/2
    for i in keyinput:
        if i == "left" and a[0]-1>=-x: 
            a[0]-=1
        elif i == "right" and a[0]+1<=x: 
            a[0]+=1
        elif i == "down" and a[1]-1>=-y: 
            a[1]-=1
        elif i == "up" and a[1]+1<=y: 
            a[1]+=1
    return a