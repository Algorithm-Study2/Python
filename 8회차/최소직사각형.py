def solution(sizes):
    answer = 0
    max_a=0 # 가로 최대값
    max_b=0 # 세로 최대값
    for i in sizes: 
        a,b=i[0],i[1] #가로 길이 세로길이를 a,b에 입력
        if a<b:
            a,b=b,a #가로길이가 더 길도록 배열을 수정
        if a>max_a: 
            max_a=a #최댓값기록
        if b>max_b:
            max_b=b #최댓값기록
    #최댓값의 넓이 반환
    return max_a*max_b
