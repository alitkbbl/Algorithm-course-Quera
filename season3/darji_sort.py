n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    p = i
    while p > 0 and a[p] < a[p-1]:
        a[p],a[p-1] = a[p-1],a[p]
        p = p-1

for item in a:
    print(item , end=' ')