n, q = list(map(int, input().split(" ")))

ps = [[0] * (n + 1) for i in range(n + 1)]

A = []
for i in range(n):
    B = list(map(int, input().split(" ")))
    for j in range(n):
        ps[i + 1][j + 1] = B[j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

for i in range(q):
    l1, r1, l2, r2 = list(map(int, input().split(" ")))
    l2 += 1
    r2 += 1
    print(ps[l2][r2] - ps[l2][r1] - ps[l1][r2] + ps[l1][r1])