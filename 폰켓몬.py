def solution(num):
  a = []
  for i in range(len(num)):
    if(num[i] not in a):
      a.append(num[i])
    if(len(num)/2 < len(a)):
      return len(num)/2
    else:
      return len(a)
