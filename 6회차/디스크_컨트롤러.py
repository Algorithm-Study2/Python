import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    time=0 #현재 시간
    total_time=0 #총 대기 시간
    a=len(jobs)
    job_queue=[] #작업대기줄
    
    while jobs or job_queue:
        # 대기열에 작업 추가
        while jobs and jobs[0][0]<=time:
            # 요청된 작업을 대기열에 추가
            request_time,job_time=jobs.pop(0)
            heapq.heappush(job_queue,(job_time,request_time))
        
        if job_queue:
            # 대기열에서 가장 소요 시간이 작은 작업을 처리
            job_time,request_time=heapq.heappop(job_queue)
            start_time=max(time,request_time)
            end_time=start_time+job_time
            total_time+=(end_time-request_time)
            time=end_time
        else:
            time=jobs[0][0]
    
    # 평균 대기 시간 계산 (소수점은 버리기 때문에 몫만)
    answer=total_time//a
    
    return answer
