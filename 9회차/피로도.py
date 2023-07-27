from itertools import permutations
def solution(k, dungeons):
    temp = 0
    count = 0
    p = k
    for pd in permutations(dungeons, len(dungeons)):
        for i in pd:
            if(k >= i[0]):
                count += 1
                k -= i[1]
            if(k == 0): break
        if(count > temp): temp = count
        k = p
        count = 0
    return temp
