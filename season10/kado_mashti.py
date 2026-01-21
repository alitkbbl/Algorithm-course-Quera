MOD = 10 ** 9 + 7


def solve():
    t, k = map(int, input().split())
    queries = []
    max_b = 0
    for _ in range(t):
        a, b = map(int, input().split())
        queries.append((a, b))
        max_b = max(max_b, b)

    dp = [0] * (max_b + 2)
    dp[0] = 1
    for i in range(1, max_b + 1):
        dp[i] = dp[i - 1]
        if i >= k:
            dp[i] = (dp[i] + dp[i - k]) % MOD
        else:
            pass  #  dp[i] = dp[i-1] from above line

    ps = [0] * (max_b + 2)
    for i in range(max_b + 1):
        ps[i] = (ps[i - 1] + dp[i]) % MOD

    for a, b in queries:
        ans = (ps[b] - ps[a - 1]) % MOD
        print(ans)


if __name__ == "__main__":
    solve()