def solution(clothes):
    answer = 1
    kind = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in kind:
            kind[clothes[i][1]] = 1
        else: kind[clothes[i][1]] += 1
    for i in kind:
        answer *= kind[i] + 1
    return answer - 1
