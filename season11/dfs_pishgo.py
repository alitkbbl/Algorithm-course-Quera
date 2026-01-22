from collections import deque

n, m = map(int, input().split())
s, t = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)
queue = deque([s])
visited[s] = True

while queue:
    v = queue.popleft()
    if v == t:
        print("YES")
        exit()
    for u in adj[v]:
        if not visited[u]:
            visited[u] = True
            queue.append(u)

print("NO")
