import sys
sys.setrecursionlimit(10**5 + 100)

from collections import deque

def bfs(start, adj, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])

    far_node = start

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[far_node]:
                    far_node = v

    return far_node, dist[far_node]


n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


u, _ = bfs(1, adj, n)

v, diameter = bfs(u, adj, n)

print(diameter)
