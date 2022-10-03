def cheak(answer):
    cnt = 0
    for m in answer:
        if len(m) == 0:
            continue
        if int(m) < 2:
            continue
            
        else:
            i = int(m)
            c = True
            for n in range(2,int(i**0.5) + 1):
                if i % n == 0:
                    c = False
                    break
            if c:
                cnt += 1
    return cnt


def solution(n, k):
    answer = ''

    while n:
        answer = str(n%k) + answer
        n //= k
    answer = answer.split('0')

    return cheak(answer)