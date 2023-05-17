def solution(priorities, location):
    a, b = [], []
    c, loc = 1, []
    for i in range(len(priorities)): loc.append(i)
    while(priorities):
        if(priorities[0] == max(priorities)):
            a.append(priorities[0])
            b.append(loc[0])
            del priorities[0]
            del loc[0]
        else:
            temp1 = priorities[0]
            temp2 = loc[0]
            del priorities[0]
            del loc[0]
            priorities.append(temp1)
            loc.append(temp2)
    for i in b:
        if(i == location): return c
        else: c += 1
