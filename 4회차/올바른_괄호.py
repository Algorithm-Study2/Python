def solution(s):
    #여 닫기를 세는 count 선언
    count=0
    #s의 글자수 만큼 반복하는데
    for i in range (len(s)):
        #s가 여는 괄호일때는 1을 더하고
        if s[i]=="(":
            count=count+1
        #s가 닫는 괄호에는 1을 뺀다.
        else:
            count=count-1
        #만약 한번이라도 음수 값이 나오면 먼저 닫는 괄호가 나오므로 False
        if count<0:
            return False
    #반복문 탈출 후 0이 나왔다면 올바른 괄호
    if count==0:
        return True
    #0이 아니라면 올바르지 않은 괄호
    else:
        return False
