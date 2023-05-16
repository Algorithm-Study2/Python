def solution(prices):
    answer=[]
    #이중 for 문으로 세는데
    for i in range(len(prices)):
        count=0 #i가 초기화 되면 0으로 count 초기화
        for j in range(i+1,len(prices)):
            count=count+1
            #가격이 i번째가 j번째보다 크면 -> 작아지면 count기록 후 break
            #없으면 끝까지 세고 count 기록
            if prices[i]>prices[j]:
                break
        answer.append(count)
    return answer
