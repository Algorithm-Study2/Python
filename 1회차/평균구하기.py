def solution(arr):
    answer = 0
    a=len(arr)
    for i in range(0,a):
        answer+=arr[i]
    answer=answer/len(arr)
    return answer
