def solution(phone_book):
    hash_map = {} #딕셔너리 선언
    for i in phone_book: #반복문을 통해 Hash map 생성 
        hash_map[i] = 1
    for i in phone_book: #book만큼 반복
        word = ""
        for number in i:
            word += number #접두어를 하나씩 추가 하면서
            if word in hash_map and word != i: #접두어면 False
                return False
    return True #아니면 True
