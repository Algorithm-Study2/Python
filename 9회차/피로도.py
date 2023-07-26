from itertools import permutations

def solution(k, dungeons):
    answer = 0
    n=len(dungeons) #던전의 길이
    
    for i in permutations(dungeons,n):
        tired=k #피로도 초기화
        count=0 
        # i는 던전의 순열
        for j in i:
            #현재 체력으로 해당 던전을클리어 가능한가? 
            if tired>=j[0]:
                #던전 클리어 후 피로도, 던전수 증가
                tired=tired-j[1]
                count+=1
            #현재까지의 최대 던전 수 반환
            if count>answer:
                answer=count
    return answer
