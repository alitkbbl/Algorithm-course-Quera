n = int(input())
ans = 0

for a in range(1, (n + 1)//2):
    for b in range(a, n + 1 - a):
        c = n - a - b
        if b <= c < a + b:
            ans += 1

print(ans)