from collections import deque

n = int(input())
start = tuple(map(int, input().split()))
target = tuple(range(1, n + 1))

# BFS
queue = deque()
queue.append(start)

dist = {start: 0}

while queue:
    cur = queue.popleft()

    if cur == target:
        print(dist[cur])
        break

    for x in range(1, n + 1):
        nxt = cur[:x][::-1] + cur[x:]
        if nxt not in dist:
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)
