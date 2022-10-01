def solution(s):
    s = list(s)
    answer = 0
    if s[0] == '-':
        answer = -int("".join(s[1:]))
    else:
        answer = int("".join(s))
    
    return answer