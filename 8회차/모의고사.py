def solution(answers):
    person_1=[1,2,3,4,5] #1번 수포자
    person_2=[2,1,2,3,2,4,2,5] #2번 수포자
    person_3=[3,3,1,1,2,2,4,4,5,5] #3번 수포자
    answer = []
    score=[0,0,0]
#정답이 일치하면 점수를 하나씩 올림
    for i in range(len(answers)):
        if answers[i]==person_1[i%5]:
            score[0]+=1
        if answers[i]==person_2[i%8]:
            score[1]+=1
        if answers[i]==person_3[i%10]:
            score[2]+=1
# 정답의 최댓값을 고른 후, 최댓값과 일치하면 answer에 append
    max_score=max(score)
    for i in range(0,3):
        if score[i]==max_score:
            answer.append(i+1)
    return answer
