def solution(n):
    answer = []
    for j in range(1,n+1):
            if n % j == 0:
                answer.append(j)
    return answer
