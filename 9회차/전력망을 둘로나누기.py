def count(a,b,temp):
    num=1
    for x in temp[a]:
        if x!=b:
            num+=count(x,a,temp)
    return num

def solution(n, wires):
    temp=[[] for i in range(n+1)]
    #인접한 전력망을 temp에 순서대로 저장
    for a,b in wires:
        temp[a].append(b)
        temp[b].append(a)
    #서브 네트워크 크기 차이의 최소값을 초기화함
    min_diff=float('inf')
    for a,b in wires:
        # 하나씩 지워보는데
        temp[a].remove(b)
        temp[b].remove(a)
        # 네트워크를 카운트 함
        count_a=count(a,b,temp)
        count_b=n-count_a
        #두 네트워크이 절대값을 구함
        diff=abs(count_a-count_b)
        #현재까지의 최솟값을 비교함
        min_diff=min(min_diff,diff)

        temp[a].append(b)
        temp[b].append(a)
        
    return min_diff
