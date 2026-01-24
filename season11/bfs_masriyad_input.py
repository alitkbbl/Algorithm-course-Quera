import sys
from collections import deque

input = sys.stdin.readline


def solve():
    line1 = input().split()
    if not line1: return
    n, m = map(int, line1)

    line2 = input().split()
    if not line2: return
    s, t = map(int, line2)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    queue = deque([s])
    dist[s] = 0

    found = False
    while queue:
        curr = queue.popleft()

        if curr == t:
            found = True
            break

        for neighbor in adj[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + 1
                parent[neighbor] = curr
                queue.append(neighbor)

    if not found:
        print("-1")
    else:
        print(dist[t])
        path = []
        curr_node = t
        while curr_node != -1:
            path.append(curr_node)
            curr_node = parent[curr_node]
        print(*(path[::-1]))


if __name__ == "__main__":
    solve()