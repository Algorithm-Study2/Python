def solution(x, n):
    answer = []
    for i in range(0,n):
        answer.append(0)
        answer[i]=x+x*i
    return answer
