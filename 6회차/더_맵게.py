import heapq

def solution(scoville, K):
    answer = 0
    heap=[]
    #heap 형식으로 스코빌을 heap에 저장
    for i in scoville:
        heapq.heappush(heap,i)
    #저장된 heap의 최소 스코빌이 K보다 작다면
    while heap[0]<K:
        #힙의 숫자가 2보다 작으면 더 섞을 수 없기 때문에 -1 리턴
        if len(heap)<2:
            return -1
        #두개의 최솟값을 섞은 값을 mix에 저장
        mix=heapq.heappop(heap)+2*heapq.heappop(heap)
        #heap에 혼합물의 스코빌을 저장
        heapq.heappush(heap,mix)
        #섞은 횟수 1추가
        answer+=1
        
    return answer

