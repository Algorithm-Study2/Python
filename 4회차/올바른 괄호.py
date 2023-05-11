def solution(s):
    answer = True
    a, b = 0, 0
    for i in s:
        if(i == '('): a += 1
        else: b += 1
        if(b > a): answer = False
    if(a != b): answer = False
    return answer
