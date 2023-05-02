def solution(genres, plays):
    answer = []
    genre = {}
    play = {}
    for i in range(len(genres)):
        if genres[i] not in genre: genre[genres[i]] = plays[i]
        else: genre[genres[i]] += plays[i]
    genre = sorted(genre.items(), key = lambda x: -x[1])
    play = [[genres[i], plays[i], i] for i in range(len(plays))]
    play = sorted(play, key = lambda x: -x[1])
    for i in genre:
        count = 0
        for j in play:
            if(j[0] == i[0]):
                count += 1
                if(count > 2): break
                else: answer.append(j[2])
    return answer
