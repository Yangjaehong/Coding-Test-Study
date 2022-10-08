from collections import deque
def bfs(graph,check,n):
    count = 0
    q = deque()
    q.append(1)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            if check[i] == 0:
                check[i] = check[now] + 1
                q.append(i)


def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    graph = [[] for _ in range((n+1))] 
    check = [0] * (n+1)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    bfs(graph,check,n)
    
    m = max(check)
    print(check)
    for i in range(2,len(check)):
        if check[i] == m:
            answer += 1
    return answer