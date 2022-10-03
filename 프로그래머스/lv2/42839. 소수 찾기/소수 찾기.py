import itertools
def check(num):
    if num == 0 or num == 1:
        return False
    
    for n in range(2,(num // 2) + 1):
        if num % n == 0:
            return False

    return True

def solution(numbers):
    
    answer = 0
    numbers = list(numbers)
    number =[]
    k = []
    for i in numbers:
        k.append(int(i))

    for i in range(len(k) + 1):
        number.append(list(map(list,itertools.permutations(numbers,i))))
    
    for i in number:
        for j in i:
            if len(j) != 0:
                k.append(int("".join(j)))

    numbers = list(set(k))

    for i in numbers:
        if check(i) == True:
            answer += 1
            
    return answer