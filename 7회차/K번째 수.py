def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k=command
        # 배열 array의 i번째부터 j번째까지를 복사하여 새로운 리스트 생성
        arr=array[i-1:j]
        # 생성한 리스트를 정렬
        arr.sort()
        # 정렬된 리스트에서 k번째 수를 answer 리스트에 추가
        answer.append(arr[k-1])
    return answer
