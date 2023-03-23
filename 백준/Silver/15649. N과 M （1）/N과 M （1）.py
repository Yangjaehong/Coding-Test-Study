def dfs(n,m):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(n,m)
        s.pop()
        visited[i] = False


n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)

dfs(n,m)