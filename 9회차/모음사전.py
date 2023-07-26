def solution(word):
    answer = 0
    for i, n in enumerate(word):
        #문자의 가능한 조합의 개수를 계산하고 결과를 더해줌
        answer += (5**(5-i)-1)/4*"AEIOU".index(n)+1
    return answer
