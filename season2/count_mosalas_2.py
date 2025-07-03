
n = int(input())
ans = 0

max_a = n // 3
for a in range(1, max_a + 1):
    upper = (n - 3 * a) // 2
    lower = max(0, (n // 2) - 2 * a + 1)
    count = upper - lower + 1
    if count > 0:
        ans += count

print(ans)