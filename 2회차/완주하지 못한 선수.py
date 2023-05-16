def solution(participant, completion):
    d = {} #빈 딕셔너리 생성
    for i in participant: #참가자의 이름을 꺼내서
        if i in d: #딕셔너리에 이름이 있는 경우에는 1을 더함 (동명이인때문에)
            d[i] += 1 
        else: #딕셔너리에 없으면 값에 1을 넣음
            d[i] = 1
    for i in completion: #완주자의 이름을 꺼내서
        d[i] -= 1 #딕셔너리에 있으면 1을 뺌
    for i in d: #딕셔너리에 값이 0이아니면 참가자엔 있으나, 완주자에 없음, 즉 1이 반환될테니
        if d[i] != 0: #0이 반환되지 않으면, 이름을 반환
            answer=i
            return answer
