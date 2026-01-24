import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    n = int(input_data[ptr]);
    ptr += 1
    m = int(input_data[ptr]);
    ptr += 1
    s = int(input_data[ptr]);
    ptr += 1
    t = int(input_data[ptr]);
    ptr += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr]);
        ptr += 1
        v = int(input_data[ptr]);
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * (n + 1)
    dist = [-1] * (n + 1)

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