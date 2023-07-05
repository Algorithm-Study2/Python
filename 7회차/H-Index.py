def solution(citations):
    answer = len(citations)
    citations.sort()
    while(citations[0] < answer):
        answer -= 1
        if(answer == 0): return 0
        citations.pop(0)
    return answer
