def solution(sizes):
    flag = 0
    if sizes[0][0] < sizes[0][1]:
        temp1 = sizes[0][1]
        temp2 = sizes[0][0]
    else:
        temp1 = sizes[0][0]
        temp2 = sizes[0][1]
    for i in sizes:
        if temp1 < i[0]:
            temp1 = i[0]
            flag = 0
        elif temp1 < i[1]:
            temp1 = i[1]
            flag = 1
    for i in sizes:
        if i[0] < i[1]:
            if temp2 < i[0]: temp2 = i[0]
        else:
            if temp2 < i[1]: temp2 = i[1] 
    return temp1*temp2
