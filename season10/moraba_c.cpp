#include <bits/stdc++.h>
using namespace std;

const int MAXN = 300;
int a[MAXN][MAXN];
int par[MAXN][MAXN];
int dp[MAXN][MAXN];
int k;

int get(int i, int j)
{
    return par[i][j] + par[i - k][j - k] - par[i][j - k] - par[i - k][j];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m >> k;

    int ans = n * m;
    for (int solve = 0; solve < 2; solve++)
    {
        int total = 0;
        if (!solve)
        {
            for (int i = 40; i < n + 40; i++)
            {
                for (int j = 40; j < m + 40; j++)
                {
                    cin >> a[i][j];
                    total += a[i][j];
                    par[i][j] = par[i - 1][j] + par[i][j - 1] - par[i - 1][j - 1] + a[i][j];
                    dp[i][j] = max(get(i, j), max(dp[i - 1][j], dp[i][j - 1]));
                }
            }
        }

        if (solve == 1)
        {
            for (int i = 40; i < n + 40; i++)
                reverse(a[i] + 40, a[i] + 40 + m);
            for (int i = 40; i < n + 40; i++)
            {
                for (int j = 40; j < 40 + m; j++)
                {
                    total += a[i][j];
                    par[i][j] = par[i - 1][j] + par[i][j - 1] - par[i - 1][j - 1] + a[i][j];
                    dp[i][j] = max(get(i, j), max(dp[i - 1][j], dp[i][j - 1]));
                }
            }
        }

        for (int i = 40; i < n + 40; i++)
        {
            for (int j = 40; j < m + 40; j++)
            {
                for (int x = i - k + 1; x <= i; x++)
                {
                    for (int y = j - k + 1; y <= j; y++)
                    {
                        int t = total - get(i, j) - get(x, y) + par[x][y] - par[i - k][y] - par[x][j - k] + par[i - k][j - k];
                        ans = min(ans, t);

                        ans = min(ans, total - get(i, j) - dp[i - k][j]);
                        ans = min(ans, total - get(i, j) - dp[i][j - k]);
                    }
                }
            }
        }
    }

    cout << n * m - ans << endl;
    return 0;
}
