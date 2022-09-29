def solution(num, k):
    num = str(num)
    k = str(k)
    answer = -1
    for i in range(len(num)):
        if num[i] == k:
            answer = i + 1
            break
    return answer