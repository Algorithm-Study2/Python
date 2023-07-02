def solution(numbers):
    # 정수를 문자열로 변환하여 숫자들을 이어붙여서 비교할 수 있도록 함
    numbers=list(map(str, numbers))
    # 3번씩 반복한 문자열을 기준으로 sort 실행 (number<1000)
    numbers.sort(key=lambda x:x*3,reverse=True)
    #[0,0,0,0]의 경우엔 0000으로 저장되는 것을 방지하기 위해 숫자로 바꿨다가 문자로 바꾸어야함
    answer=str(int(''.join(numbers)))
    return answer
