def solution(numbers):
    max=0
    for idx, i in enumerate(numbers):
        for jdx, j in enumerate(numbers):
            #if numbers[idx] != numbers[jdx]:
            if idx != jdx:
                if i*j>=max:
                    max=i*j
    return max