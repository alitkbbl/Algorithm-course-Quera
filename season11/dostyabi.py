import sys
sys.setrecursionlimit(10**5 + 100)

from collections import deque

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

q = int(input())
people = [int(input()) for _ in range(q)]

# BFS from node 1
dist = [-1] * (n + 1)
queue = deque([1])
dist[1] = 0

while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

# Find best node
best_dist = float('inf')
best_node = None

for x in people:
    if dist[x] < best_dist:
        best_dist = dist[x]
        best_node = x
    elif dist[x] == best_dist and x < best_node:
        best_node = x

print(best_node)
