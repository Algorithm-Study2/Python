def solution(brown, yellow):
    a = (brown - 4)/2
    row = (a + (a**2 - 4*yellow)**0.5)/2 + 2
    col = (a - (a**2 - 4*yellow)**0.5)/2 + 2
    return [row, col]
