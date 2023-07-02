def solution(citations):
    answer = 0
    #높은 숫자가 앞에오도록 sort()
    citations.sort(reverse=True)
    #배열의 길이만큼 반복
    for i in range(len(citations)):
        #만약에 i+1, h번 이상인용된 논문이 있다면 answer에 h를 넣고
        if citations[i]>=i+1:
            answer=i+1
        #아니면 앞의 answer를 반환
        else:
            break
    return answer
