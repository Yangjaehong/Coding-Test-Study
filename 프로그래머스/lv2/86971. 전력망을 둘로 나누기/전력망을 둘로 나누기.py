from collections import deque
def bfs (v,n, graph, visited):
    visited[v] = True
    cnt = 1
    q = deque()
    q.append(v)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == False:
                cnt += 1
                q.append(i)
                visited[i] = True
    return cnt

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    
    for v, cut in wires:
        visited = [False] * (n+1)
        visited[cut] = True
        result = bfs(v,n,graph,visited)


        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))

    return answer