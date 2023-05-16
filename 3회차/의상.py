def solution(clothes):
    hash_map={}
    for name,kind in clothes:
        if kind not in hash_map:
            hash_map[kind]=1
        else:
            hash_map[kind]+=1
    print(hash_map)
    answer=1
    for i in hash_map.keys():
        k=hash_map[i]+1
        answer=answer*k
    answer=answer-1
    return answer
    
