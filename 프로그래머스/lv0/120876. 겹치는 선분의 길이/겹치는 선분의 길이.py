# def solution(lines):
#     answer = 0
#     dat=[0]*201
#     for i in lines:
#         for j in range(i[0],i[1]+1):
#             dat[j+100]+=1
#     # print(dat)
#     for d in range(1,len(dat)):
#         if dat[d-1] >1 and dat[d] >1:
#             answer+=1
#     if answer>0:
#         if lines[0][1] == lines[1][0] and lines[1][1] == lines[2][0]:
#             answer-=1    
#     return answer

def solution(lines):
    answer = 0
    dat=[0]*200
    for i in lines:
        for j in range(i[0],i[1]):
            dat[j+100]+=1
    for n in dat:
        if n>1:
            answer+=1    
    return answer