def solution(arr):
    answer = [arr[0]]
    for i in range(len(arr) - 1):
        if(arr[i + 1] != arr[i]):
            answer.append(arr[i + 1])
    return answer
