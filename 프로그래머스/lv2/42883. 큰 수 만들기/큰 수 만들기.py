def solution(number, k):

    answer = []
    for i in range(len(number)):
        
        if i+k+1 > len(number):
            tmp = len(number)
        else:
            tmp = i+k+1
        if i+1 == tmp:
            break
        
        if number[i] != '9':
            for j in range(i+1,tmp):
                if number[i] < number[j]:
                    answer.append(i)
                    k -= 1
                    break
            if k == 0:
                break
    
    if len(answer) == 0:
        return "".join(number[:-k])
    
    c = ''
    tmp = 0

    j = 0
    for i in range(len(number)):
        if tmp == 1:
            c += number[i]
        elif answer[j] != i and tmp == 0:
            c += number[i]
        else:
            j+=1
        
        if j == len(answer):
            tmp = 1
    return c
                