import heapq

def solution(operations):
    arr=[]
    #command와 num으로 나누고, num을 숫자로 다시 선언
    for i in operations:
        command,num=i.split()
        num=int(num)
        #만약에 커맨드가 I라면 arr에 삽입
        if command=="I":
            heapq.heappush(arr,num)
        #만약에 커맨드가 D이고 num이 1이면 최댓값을 삭제
        elif command=="D" and num==1:
            if arr:
                max_val=max(arr)
                arr.remove(max_val)
        #만약에 커맨드가 D이고 num이 -1이면 최솟값을 삭제
        elif command=="D" and num==-1:
            if arr:
                min_val=min(arr)
                arr.remove(min_val)
    #만약에 배열이 있으면 최댓값과 최솟값을 반환
    if arr:
        return [max(arr),min(arr)]
    #없으면 0을 반환
    else:
        return [0,0]
