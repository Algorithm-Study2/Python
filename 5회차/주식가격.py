from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while(prices):
        period = 0
        price = prices.popleft()
        for i in prices:
            period += 1
            if(price > i):
                break
        answer.append(period)
    return answer
