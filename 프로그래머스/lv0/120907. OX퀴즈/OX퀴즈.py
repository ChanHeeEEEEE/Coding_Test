def solution(quiz):
    answer = []
    # for i in quiz:
    #     if i.replace("=","==").replace('"',""):            
    #         answer.append("O")
    #     else:
    #         answer.append("X") 
    for i in quiz:
        i=i.replace("=","==")
        if eval(i):
            answer.append("O")
        else:
            answer.append("X")
    return answer