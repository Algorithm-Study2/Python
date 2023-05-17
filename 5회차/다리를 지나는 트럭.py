def solution(bridge_length, weight, truck_weights):
    answer, truck = 0, 0
    bridge = [0] * bridge_length
    while(bridge):
        answer += 1
        truck -= bridge[0]
        bridge.pop(0)
        if(truck_weights):
            if(truck + truck_weights[0] > weight):
                bridge.append(0)
            else:
                truck += truck_weights[0]
                bridge.append(truck_weights.pop(0))
    return answer
