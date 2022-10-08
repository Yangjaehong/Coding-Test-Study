from collections import deque

def bfs(node,check):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if check[i] == 0:
                check[i] = check[node] + 1
                q.append(i)



n = int(input())
v, u = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
check = [0] * (n+1)
for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(v, check)
if check[u] == 0:
    print(-1)
else:
    print(check[u])

