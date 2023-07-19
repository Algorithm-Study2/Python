def solution(answers):
    answer = []
    temp1, temp2, temp3 = 0, 0, 0
    gum1 = [1, 2, 3, 4, 5]
    gum2 = [2, 1, 2, 3, 2, 4, 2, 5]
    gum3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    location = 0
    for i in answers:
        location += 1
        if i == gum1[location%5 - 1]: temp1 += 1
        if i == gum2[location%8 - 1]: temp2 += 1
        if i == gum3[location%10 - 1]: temp3 += 1
    solution = max(temp1, temp2, temp3)
    if temp1 == solution: answer.append(1)
    if temp2 == solution: answer.append(2)
    if temp3 == solution: answer.append(3)
    return answer
