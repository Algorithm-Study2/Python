import math
def solution(brown, yellow):
    carpet=brown+yellow #전체 타일 개수
    c=math.sqrt(carpet) 
    c=math.ceil(c) #제곱근을 구하고 올림
    #역순으로 탐색하는데
    for i in range(c,0,-1):
        #전체 타일개수가 나눠 떨어지면서, yellow가 안쪽에 있을 때 반환함
        if carpet%i==0 and yellow>=(i-2)*(carpet/(i)-2):
            return [max(i,carpet/i),min(i,carpet/i)]
