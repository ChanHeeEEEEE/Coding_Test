def solution(n):
    answer = 0
    for i in range(1,n+1):
#         s=str(i)
        
#         if "3" in s:
#             answer+=1
#         if i%3 ==0:
#             answer+=1
        answer+=1
        while "3" in str(answer) or (answer%3==0):
            # k=str(answer)
            # if "3" in k:
            #     answer+=1
            # elif answer//3 ==0:
            #     answer+=1
            answer+=1
        print(answer)
    return answer