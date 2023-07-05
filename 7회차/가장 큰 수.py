def solution(numbers):
    answer = []
    count = 0
    for i in numbers:
        if(i == 0): count += 1
        answer.append(str(i))
    answer.sort(key=lambda x:x*3, reverse=True)
    if(count == len(numbers)): return "0"
    else: return ''.join(answer)
