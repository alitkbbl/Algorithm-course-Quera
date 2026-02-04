import sys

sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    h = list(map(int, input_data[1:]))

    if n == 0:
        print(0)
        return

    sorted_h = sorted(list(set(h)))
    rank_map = {val: i for i, val in enumerate(sorted_h)}
    h = [rank_map[x] for x in h]
    m = len(sorted_h)

    MOD = 10 ** 9 + 7

    dp = [[[0] * (m + 1) for _ in range(n)] for _ in range(n)]

    for k in range(m - 1, -1, -1):
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if length == 1:
                    res = 1
                elif length == 2:
                    term1 = dp[l][r - 1][k]
                    term2 = dp[l + 1][r][k]
                    term3 = 1
                    res = (term1 + term2 - term3) % MOD
                else:
                    term1 = dp[l][r - 1][k]
                    term2 = dp[l + 1][r][k]
                    term3 = dp[l + 1][r - 1][k]
                    res = (term1 + term2 - term3) % MOD

                if h[l] == h[r] and h[l] >= k:
                    inner_k = h[l]

                    if length <= 2:
                        inner_val = 1
                    else:
                        inner_val = dp[l + 1][r - 1][inner_k]

                    res = (res + inner_val) % MOD

                dp[l][r][k] = res

    ans = (dp[0][n - 1][0] - 1 + MOD) % MOD
    print(ans)


if __name__ == '__main__':
    solve()