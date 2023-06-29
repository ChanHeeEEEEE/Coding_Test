def solution(board):
    answer = 0
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]
    n=len(board)
    temp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                temp[i][j]+=1
                for x in dx:
                    for y in dy:
                        ix=i+x
                        jy=j+y
                        if ix>=0 and ix<n and jy>=0 and jy<n:
                            temp[ix][jy]+=1
    answer=n*n
    for i in range(n):
        for j in range(n):
            if temp[i][j] != 0:
                answer-=1 
    return answer
# def solution(board):
#     answer = 0
#     x=len(board[0])
#     y=len(board)
#     temp = [[0]*x for i in range(y)]
#     for i in range(y):
#         for j in range(x):
#             if board[i][j] != 0:
#                 temp[i][j] +=1
#                 if i-1>=0 and j-1>=0 and i+1<y and j+1 <x:
#                     temp[i-1][j-1] +=1
#                     temp[i-1][j] +=1
#                     temp[i-1][j+1] +=1
#                     temp[i][j-1] +=1
#                     temp[i][j+1] +=1
#                     temp[i+1][j-1] +=1
#                     temp[i+1][j] +=1
#                     temp[i+1][j+1] +=1
#     t_x=len(temp[0])
#     t_y=len(temp)
#     answer=x*y
#     for i in range(t_y):
#         for j in range(t_x):
#             if temp[i][j] != 0:
#                 answer-=1   
#     return answer
# def solution(board):
#     answer = 0
#     x=len(board[0])
#     y=len(board)
#     temp = [[0]*x for i in range(y)]
#     for i in range(y):
#         for j in range(x):
#             if board[i][j] != 0:
#                 temp[i][j] +=1
#                 if i-1>=0 and j-1>=0:
#                     temp[i-1][j-1] +=1
#                 elif i-1>=0:
#                     temp[i-1][j] +=1
#                 elif i-1>=0 and j+1 <x:
#                     temp[i-1][j+1] +=1
#                 elif j-1>=0:
#                     temp[i][j-1] +=1
#                 elif j+1 <x:
#                     temp[i][j+1] +=1
#                 elif i+1< y & j-1>=0:
#                     temp[i+1][j-1] +=1
#                 elif i+1< y:
#                     temp[i+1][j] +=1
#                 elif i+1<y & j+1 <x:
#                     temp[i+1][j+1] +=1
#     # print(temp)
#     t_x=len(temp[0])
#     t_y=len(temp)
#     answer=x*y
#     for i in range(t_y):
#         for j in range(t_x):
#             if temp[i][j] != 0:
#                 answer-=1   
#     return answer