def binary_search(search, v):
    start = 0
    end = len(search) - 1
    while start <= end:
        mid = (start + end) // 2

        if search[mid] == v:
            print(1)
            return 0

        elif search[mid] > v:
            end = mid - 1

        else:
            start = mid + 1

    print(0)
    return 0

n = int(input())
search = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

search.sort()
for i in target:
    binary_search(search,i)
