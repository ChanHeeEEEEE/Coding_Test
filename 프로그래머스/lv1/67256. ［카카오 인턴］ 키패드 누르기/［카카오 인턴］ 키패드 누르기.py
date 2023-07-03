def solution(numbers, hand):
    answer = ''
    dic = {"1": (1,1), "2" : (1,2), "3": (1,3),"4":(2,1),"5":(2,2),
          "6":(2,3),"7":(3,1),"8":(3,2),"9":(3,3),"*":(4,1),"0":(4,2),"#":(4,3)}
    L = dic["*"]
    R = dic["#"]
    for i in numbers:
        if i in [1,4,7]:
            answer+="L"
            L=dic[str(i)]
        elif i in [3,6,9]:
            answer+="R"
            R=dic[str(i)]
        else:
            d=abs(R[0]-dic[str(i)][0])+abs(R[1]-dic[str(i)][1])
            dd=abs(L[0]-dic[str(i)][0])+abs(L[1]-dic[str(i)][1])
            print(d,dd)
            if d<dd:
                answer+="R"
                R=dic[str(i)]
            elif d>dd:
                answer+="L"
                L=dic[str(i)]
            else:
                if hand== "right":
                    answer+="R"
                    R=dic[str(i)]
                else:
                    answer+="L"
                    L=dic[str(i)]

        

    return answer