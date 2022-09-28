def solution(s):
    
    s = list(s)
    
    if (s.count('p') + s.count('P')) == s.count('y') +s.count('Y'):
        return True
        
    else: return False