def solution(genres,plays):
    total={}
    song={}
    count={}
    answer=[]
    c=0
    for i in genres:
        if i not in total:
            total[i]=0
            song[i]=[]
        total[i]+=plays[c]
        song[i].append((c,plays[c]))
        c=c+1
    sorted_genre=sorted(total,key=lambda x:total[x],reverse=True)
    for i in sorted_genre:
        count=sorted(song[i],key=lambda x: (-x[1],x[0]))
        for j in range(min(len(song[i]),2)):
            answer.append(count[j][0])
    return answer
