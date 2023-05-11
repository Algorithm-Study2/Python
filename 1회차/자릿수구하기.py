def solution(n):
    answer = 0
    while n>0.5:
        ans=n%10
        answer+=ans
        n=n//10
    return answer
