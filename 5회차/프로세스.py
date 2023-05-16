def solution(priorities, location):
    answer = 0
    # 튜플 생성하는 데 (index, priorities)로 생성
    queue=[(i, p) for i,p in enumerate(priorities)]
    while queue:
        #order에는 튜플 하나씩 들어오는데, 그 값은 맨 앞의 값을 받고 그 값을 queue에서 삭제함.
        order=queue[0]
        queue.pop(0)
        #만약에 order에 들어온 우선 순위가 queue의 모든 우선순위보다 낮으면?
        if any(order[1]<q[1] for q in queue):
            #맨 마지막으로 채워넣음
            queue.append(order)
        #만약 order에 들어온 우선순위가 queue에 있는 모든 우선순위보다 높으면?
        else:
            #실행순서를 하나 더하고
            answer=answer+1
            #만약에 내가 찾는 위치의 우선 순위가 실행되면 반복문 탈출
            if order[0]==location:
                break
    return answer
