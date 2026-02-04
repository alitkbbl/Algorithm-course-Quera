MOD = 10**9 + 7
MAX = 2000

fact = [1] * (MAX + 1)
inv = [1] * (MAX + 1)

for i in range(1, MAX + 1):
    fact[i] = (fact[i - 1] * i) % MOD

inv[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX - 1, -1, -1):
    inv[i] = (inv[i + 1] * (i + 1)) % MOD

def tarkib(n, r):
    if r > n:
        return 0
    return (fact[n] * inv[r] % MOD) * inv[n - r] % MOD

q = int(input())

for _ in range(q):
    n, r = map(int, input().split())
    print(tarkib(n, r))
