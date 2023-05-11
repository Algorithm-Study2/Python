def solution(progresses, speeds):
    import math
    answer=[]
    days=[]
    #math를 이용해 소요 날짜를 배열로 만듦
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    #카운트로 개수를 세고, 몇개의 날이 한번에 갈수 있는 지 계산하고
    count=1
    for i in range(len(days)-1):
        if days[i-count+1]<days[i+1]:
            answer.append(count)
            count=1
        else:
            count=count+1
    #마지막날짜를 포함시킴
    answer.append(count)
    return answer
