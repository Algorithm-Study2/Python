def solution(bridge_length, weight, truck_weights):
    sec=1 #시간
    ing=[] #다리위에 지나가는 트럭의 무게
    time=[] #지나가기 시작하는 시간
    i=1 #순서 번호
    ing.append(truck_weights[0]) #첫항의 트럭 무게
    time.append(1) #첫번째 지나가는 시간
    #무한 반복
    while True:
        #모든 차량이 다 지나가면 break
        if i==len(truck_weights):
                break
        sec=sec+1 #시간이 지나갑니다.
        #지나가기 시작하는 시간 + bridge_length의 합이 sec과 같으면
        if time[0]+bridge_length==sec:
            ing.pop(0) #차의 무게 사라지게 만들고
            time.pop(0) #들어온 차의 시간도 사라지게 만듦
        if sum(ing)+truck_weights[i]<=weight: #무게가 만약에 작으면
            ing.append(truck_weights[i]) #다음 차량도 들어올 수 있게 만들고
            time.append(sec) #시간도 기록해 둔다.
            i=i+1 #대기 차량 번호 하나 더 올린다.
    return sec+bridge_length #들어오는 시간이 나오므로, 마지막 차량이 지나가는 시간
