n, q = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        prefix[i + 1][j + 1] = matrix[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    total = (prefix[x2 + 1][y2 + 1] - prefix[x1][y2 + 1] - prefix[x2 + 1][y1] + prefix[x1][y1])
    print(total)