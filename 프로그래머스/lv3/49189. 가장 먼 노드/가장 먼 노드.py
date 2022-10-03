from collections import deque
def bfs(graph,visited,n):
    count = 0
    q = deque([[1,count]])
    
    while q:
        now, count = q.popleft()
        
        if visited[now] == -1:
            visited[now] = count
            count += 1
            for i in graph[now]:
                q.append([i, count])


def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    graph = [[] for _ in range((n+1))] 
    
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    bfs(graph,visited,n)
    
    m = max(visited)
    for i in visited:
        if i == m:
            answer += 1
    return answer