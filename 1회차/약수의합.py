def solution(n):
    answer = 0
    arr=[]
    count=0
    for i in range(1,n+1):
        if n%i==0:
            arr.append(0)
            arr[count]=i
            count=count+1
    for i in range(0,count):
        answer+=arr[i]
    return answer
