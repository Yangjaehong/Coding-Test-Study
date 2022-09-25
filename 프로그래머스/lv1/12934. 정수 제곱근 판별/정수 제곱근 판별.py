import math

def solution(n):
    answer = int(math.sqrt(n))
    answer *= answer 
    
    if answer == n:
        answer = int(math.sqrt(n)) + 1
        answer *= answer
        
    else: answer = -1
    
    return answer