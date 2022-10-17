from collections import deque
def ck(q):
    temp = []
    for word in q:
        if word =='{' or word =='[' or word =='(':
            temp.append(word)
        elif word =='}' or word ==']' or word ==')':
            if len(temp) == 0:
                return False
            if word == '}' and temp[-1] == '{':
                temp.pop()
            elif word == ']' and temp[-1] == '[':
                temp.pop()
            elif word == ')' and temp[-1] == '(':
                temp.pop()
    if temp:
        return False
    else:
        return True
    
    
def solution(s):
    answer = 0
    q = deque(s)
    if len(s) == 0:
        return 0
    if ck(q):
        answer += 1
    for i in range(len(q) -1):
        q.append(q.popleft())
        if ck(q):
            answer += 1
    return answer