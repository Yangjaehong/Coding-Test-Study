def fib(n):
    arr = [0,1]
    if n < 2:
        return arr[n]
    else:
        for i in range (2,n+1):
            arr.append(arr[i-2] + arr[i-1])
        return arr[-1]
    
def solution(n):
    a = 1234567
    answer = fib(n) % a
    return answer