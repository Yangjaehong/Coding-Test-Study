def solution(priorities, location):
    answer = 0
    name = [i for i in range(len(priorities))]
    print(name)
    while True:
        if priorities[0] < max(priorities):
            temp = priorities.pop(0)
            priorities.append(temp)
            temp = name.pop(0)
            name.append(temp)
        else:
            answer += 1
            priorities.pop(0)
            temp = name.pop(0)
            if temp == location:
                break
    return answer