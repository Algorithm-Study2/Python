import heapq as hq
def solution(operations):
    minheap, maxheap = [], []
    for i in operations:
        sp = i.split()
        temp = int(sp[1])
        if(sp[0] == 'I'):
            hq.heappush(minheap, temp)
            hq.heappush(maxheap, -temp)
        else:
            if(len(minheap) > 0):
                if(temp == -1):
                    mintemp = -hq.heappop(minheap)
                    maxheap.remove(mintemp)
                else:
                    maxtemp = -hq.heappop(maxheap)
                    minheap.remove(maxtemp)
    if(minheap): return [-hq.heappop(maxheap), hq.heappop(minheap)]
    else: return [0, 0]
