#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9 + 10, MAXN = 5005, MAXS = 5005;

int dp[MAXN][MAXS], par[MAXN][MAXS];
// dp[i][j] : maximum number of toys with 'j' tomans from packages [0 .. i-1]
int n, S, c[MAXN][MAXN], cnt[MAXN];

int main()
{
    cin >> n >> S;
    for (int i = 0; i < n; i++)
    {
        cin >> cnt[i];
        for (int j = 0; j < cnt[i]; j++)
            cin >> c[i][j];
    }

    // fill the base of dp:
    for (int i = 0; i <= S; i++)
        dp[0][i] = 0;

    for (int i = 1; i <= n; i++)
    {
        for (int s = 0; s <= S; s++)
        { // fill dp[i][s] :
            dp[i][s] = dp[i - 1][s];
            par[i][s] = 0; // initially we take nothing of this package
            int sumOfCosts = 0;
            for (int j = 0; j < cnt[i - 1]; j++)
            {
                if (c[i - 1][j] <= s && dp[i][s] < dp[i - 1][s - c[i - 1][j]] + 1)
                {
                    // in case we take one of them
                    dp[i][s] = dp[i - 1][s - c[i - 1][j]] + 1;
                    par[i][s] = 1;
                }
                sumOfCosts += c[i - 1][j];
            }

            if (sumOfCosts <= s && dp[i][s] < dp[i - 1][s - sumOfCosts] + cnt[i - 1])
            {
                // in case we take all of them
                dp[i][s] = dp[i - 1][s - sumOfCosts] + cnt[i - 1];
                par[i][s] = 2;
            }
        }
    }

    cout << dp[n][S] << '\n';
    string outputPackages = "";
    for (int i = n; i > 0; i--)
    { // filling up the answer string:
        outputPackages = char('0' + par[i][S]) + outputPackages;
        if (par[i][S] == 1)
        { // if we take one we surely take the minimum cost:
            int minimum = INF;
            for (int j = 0; j < cnt[i - 1]; j++)
                minimum = min(minimum, c[i - 1][j]);
            S -= minimum;
        }
        else if (par[i][S] == 2)
        {
            int sumOfCosts = 0;
            for (int j = 0; j < cnt[i - 1]; j++)
                sumOfCosts += c[i - 1][j];
            S -= sumOfCosts;
        }
    }
    cout << outputPackages << endl;

    return 0;
}