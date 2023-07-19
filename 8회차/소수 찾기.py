from itertools import permutations
def solution(numbers):
    count = 0
    num = [i for i in numbers]
    per = []
    for i in range(len(numbers)):
        per += list(permutations(num, i + 1))
    nums = [int("".join(i)) for i in per]
    nums = list(set(nums))
    for i in nums:
        flag = 1
        if i != 0 and i != 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    flag = 0
                    break
            if flag: count += 1
    return count
