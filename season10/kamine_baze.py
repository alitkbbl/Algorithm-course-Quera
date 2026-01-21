import math

n, q = map(int, input().split())
arr = list(map(int, input().split()))

k_max = math.floor(math.log2(n)) + 1

RMQ = [[0] * n for _ in range(k_max + 1)]

for i in range(n):
    RMQ[0][i] = arr[i]

for k in range(1, k_max + 1):
    length = 1 << k
    half_length = 1 << (k - 1)
    for i in range(n - length + 1):
        RMQ[k][i] = min(RMQ[k - 1][i], RMQ[k - 1][i + half_length])

for _ in range(q):
    l, r = map(int, input().split())

    length = r - l + 1
    k = math.floor(math.log2(length))
    ans = min(RMQ[k][l], RMQ[k][r - (1 << k) + 1])

    print(ans)