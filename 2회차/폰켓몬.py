def solution(nums):
    ans = 1
    nums.sort() #sort를 통해 num을 낮은수부터 높은수로 정리
    num=len(nums) #개수를 세고
    for i in range(0,num-1): #반복문을 종류가 몇개인지 세는 코드
        if nums[i]!=nums[i+1]:
            ans=ans+1
    if ans>num//2: #그 값이 절반보다 크면 종류가 개수의 반에 해당하고
        answer=num//2
    else:#크면 종류개수에 해당함
        answer=ans
    return answer
