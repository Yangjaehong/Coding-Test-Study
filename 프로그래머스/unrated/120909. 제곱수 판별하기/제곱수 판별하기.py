def solution(n):
    for i in range(1,n):
        if n == i * i:
            return 1
    return 2