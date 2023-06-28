# def solution(polynomial):
#     answer = ''
#     pol= polynomial.split()
#     x=0
#     c=0
#     for i in pol:
#         if "x" in i:
#             x+=1
#             i=i.replace('x', '')
#             if i!="":
#                 x+=int(i)
#             else:
#                 x-=1
#         elif i == "+":
#             pass
#         else:
#             c+=int(i)
#     print(x,c)
#     if x==0 & c==0:
#         pass
#     elif x!=0 & c==0:
#         answer+=str(x)+"x"
#     elif x==0 & c!=0:
#         answer+=str(c)
#     else:
#         answer+=str(x)+"x"+" + "+str(c) 
#     return answer
def solution(polynomial):    
    pol= polynomial.split()  
    x=[]
    c=[]
    for i in pol:
        if i == "+":
            pass
        elif "x" in i:
            x.append(i)
        else:
            c.append(int(i))
    sum_x =0
    # print(x)
    for j in x:
        if len(j) ==1:
            j=j.replace('x', '1')
        else:
            j=j.replace('x', '')            
        sum_x+=int(j)
    sum_c=sum(c)
    if sum_x==1:
        sum_x=""
    if sum_x==0:
        answer =str(sum_c)
    elif sum_c ==0:
        answer =str(sum_x)+"x"
    else:
        answer =str(sum_x)+"x"+" + "+str(sum_c)
    return answer