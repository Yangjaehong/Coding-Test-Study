from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    visited[x][y] = True
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))

t = int(input())
answer = []
while t:
    cnt = 0
    t -= 1
    n, m, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    for i in range(k):
        u1, u2 = map(int, input().split())
        graph[u2][u1] = 1

    for i in range(m):
        for j in range(n):
            if visited[i][j] == False and graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    answer.append(cnt)

for i in answer:
    print(i)

