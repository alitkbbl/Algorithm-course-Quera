import sys
sys.setrecursionlimit(10**6)

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

n = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

graph = [[] for _ in range(n)]

for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        if x1 == x2 or y1 == y2:
            graph[i].append(j)
            graph[j].append(i)

visited = [False] * n
components = 0

for i in range(n):
    if not visited[i]:
        components += 1
        dfs(i)

print(components - 1)
