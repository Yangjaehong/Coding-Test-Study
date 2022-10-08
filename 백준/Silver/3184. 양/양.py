from collections import deque
def bfs(x,y,graph,visited):
    q = deque()
    q.append((x,y))
    o = 0
    v = 0
    visited[x][y] = True
    if graph[x][y] == 'o':
        o += 1
    elif graph[x][y] == 'v':
        v += 1


    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == False and graph[nx][ny] != '#':
                    if graph[nx][ny] == 'o':
                        o += 1
                    elif graph[nx][ny] == 'v':
                        v += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return o, v


dx = [-1,1,0,0]
dy = [0,0,1,-1]
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(str,input())))
visited = [[False] * m for _ in range(n)]
answer = [0,0]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] != '#' and visited[i][j] == False:
            o, v = bfs(i,j,graph,visited)
            if o > v:
                v = 0
            else:
                o = 0
            answer[0] += o
            answer[1] += v


print(*answer)