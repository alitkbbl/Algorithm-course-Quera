n, k = map(int, input().split())
c = list(map(int, input().split()))

if k >= 3:
    print(min(c))

elif k == 2:
    money = 5000
    for i in range(1, n):
        money = min(money, min(max(c[:i]), max(c[i:])))
    print(money)

else:
    print(max(c))
