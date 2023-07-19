from itertools import permutations

def solution(numbers):
    answer = []
    # numbers를 하나씩 자른 배열
    nums = [n for n in numbers]
    per = []
    # numbers의 각 숫자들을 순열로 모든 경우 만들기
    for i in range(1, len(numbers)+1):
        # i개씩 순열조합
        per += list(permutations(nums, i))
    # 각 순열조합을 하나의 int형 숫자로 변환
    new_nums = [int(("").join(p)) for p in per]

    for n in new_nums:                            
        #2보다 작으면 소수가 아님
        if n < 2:                                 
            continue
        check = True            
        # n의 제곱근 보다 작은 숫자까지만 나눗셈
        for i in range(2,int(n**0.5) + 1): 
            # 만약에 나눠 떨어지는 게 있으면 소수 아님
            if n%i==0:                        
                check=False
                break
        # 소수라면 answer에 append
        if check:
            answer.append(n)

    return len(set(answer))    
