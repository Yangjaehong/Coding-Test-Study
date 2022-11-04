from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    l = len(queue1) * 3
    target = (sum(queue1) + sum(queue2)) // 2
    a, b = sum(queue1), sum(queue2)
    while True:
        if a > target:
            cnt += 1
            a -= queue1[0]
            b += queue1[0]
            queue2.append(queue1.popleft())
        elif b > target:
            cnt += 1
            b -= queue2[0]
            a += queue2[0]
            queue1.append(queue2.popleft())
            
        elif a == b:
            return cnt
        if cnt > l:
            return -1
            