def solution(progresses, speeds):
    answer = []
    b = [1]
    for i in range(len(speeds)):
        a = (100 - progresses[i]) // speeds[i]
        if((100 - progresses[i]) % speeds[i] != 0):
            a += 1
        answer.append(a)
    c = answer[0]
    for i in range(len(answer) - 1):
        if(c >= answer[i + 1]):
            b[-1] += 1
        else:
            b.append(1)
            c = answer[i + 1]
    return b
