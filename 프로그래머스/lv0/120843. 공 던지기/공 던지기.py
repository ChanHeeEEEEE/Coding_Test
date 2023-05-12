# 인덱스로 생각
def solution(numbers, k):
    return numbers[(2*k-2)%len(numbers)]