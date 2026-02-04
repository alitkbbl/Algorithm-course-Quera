#include <bits/stdc++.h>

using namespace std;

constexpr int N = 1e5;
constexpr int MOD = 1000000007;

long long a, b, k, q, ps[N + 10], dp[N + 10];

int main()
{
    cin >> q >> k;

    dp[0] = 1;
    ps[0] = 1;
    for (int i = 1; i <= N; i++)
    {
        dp[i] = dp[i - 1];
        if (i >= k)
            dp[i] += dp[i - k];
        dp[i] %= MOD;
        ps[i] = (ps[i - 1] + dp[i]) % MOD;
    }

    for (int i = 0; i < q; i++)
    {
        cin >> a >> b;
        cout << ((ps[b] - ps[a - 1] % MOD) + MOD) % MOD << '\n';
    }

    return 0;
}
