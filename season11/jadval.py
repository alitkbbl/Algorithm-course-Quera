import sys
sys.setrecursionlimit(10**7)

n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

# 8-direction moves
dirs = [(-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)]

peaks = 0
valleys = 0

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue

        # start a new block
        stack = [(i, j)]
        visited[i][j] = True
        height = h[i][j]

        is_peak = True
        is_valley = True

        while stack:
            x, y = stack.pop()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if h[nx][ny] == height:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                    else:
                        if h[nx][ny] > height:
                            is_peak = False
                        if h[nx][ny] < height:
                            is_valley = False

        if is_peak:
            peaks += 1
        if is_valley:
            valleys += 1

print(peaks, valleys)
