def solution(n):
    abc = []
    for i in range(1, n + 1):
        if(n % i == 0):
            abc.append(i)
    answer = sum(abc)
    return answer
