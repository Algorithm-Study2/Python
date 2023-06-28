import heapq as hq
def solution(jobs):
    heap = []
    cnt, time, waste = 0, 0, 0
    start = -1
    while(cnt < len(jobs)):
        for i in jobs:
            if(start < i[0] <= time):
                hq.heappush(heap, [i[1], i[0]])
        if(len(heap) > 0):
            c = hq.heappop(heap)
            start = time
            time += c[0]
            waste += (time - c[1])
            cnt += 1
        else: time += 1
    answer = waste // cnt
    return answer
