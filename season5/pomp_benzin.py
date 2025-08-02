n, k, L = map(int, input().split())
arr_d = list(map(int, input().split()))

arr_d.append(L)

pomp = []
last_refill = 0
current = 0

for i in range(len(arr_d)):
    dist = arr_d[i] - last_refill

    if dist > k:
        print(-1)
        exit(0)

    if i < len(arr_d) - 1 and arr_d[i + 1] - last_refill > k:
        pomp.append(i + 1)
        last_refill = arr_d[i]

print(len(pomp))
if len(pomp) > 0:
    print(*pomp)
