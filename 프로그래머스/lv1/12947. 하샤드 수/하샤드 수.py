def solution(x):
    answer = True
    k = list(str(x))
    sum = 0
    for i in range(len(k)):
        sum += int(k[i])
        
    if x % sum == 0:
        answer = True
    else: answer = False
    
    return answer