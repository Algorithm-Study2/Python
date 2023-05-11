def solution(s):
    p_count=0
    y_count=0
    for i in range(0,len(s)):
        if s[i]=='p' or s[i]=='P':
            p_count=p_count+1
        if s[i]=='y' or s[i]=='Y':
            y_count=y_count+1
    return p_count==y_count
