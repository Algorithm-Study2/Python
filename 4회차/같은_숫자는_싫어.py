def solution(arr):
    #answer 배열 형성
    answer=[] 
    for i in range(len(arr)-1):
        #다음 요소와 다르면 배열을 채워넣음
        if arr[i]!=arr[i+1]: 
            answer.append(arr[i])
    #마지막 요소만 하나 더 추가로 채워 넣음
    answer.append(arr[len(arr)-1])
    return answer
