def solution(s):
    answer = len(s)  # 초기값은 문자열의 길이로 설정
    n = len(s)

    for i in range(1, n // 2 + 1):
        lst = [s[j:j + i] for j in range(0, n, i)]
        compressed = ""
        count = 1

        for k in range(1, len(lst)):
            if lst[k - 1] == lst[k]:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)
                compressed += lst[k - 1]
                count = 1

        if count > 1:
            compressed += str(count)
        compressed += lst[-1]

        answer = min(answer, len(compressed))

    return answer