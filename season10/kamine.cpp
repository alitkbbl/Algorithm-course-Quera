#include <bits/stdc++.h>
using namespace std;
const int MAX_N = 1000010;
const int LOG_MAX_N = 21; // 2^(LOG_MAX_N-1) >= MAX_N
const int INF = 1000000000;
int a[MAX_N];
int rmq[LOG_MAX_N][MAX_N];

int main()
{
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        rmq[0][i] = a[i];
    }

    for (int k = 1; k < LOG_MAX_N; k++)
        for (int i = 0; i < n; i++)
            if (i + (1 << (k - 1)) < n)
                rmq[k][i] = min(rmq[k - 1][i], rmq[k - 1][i + (1 << (k - 1))]);
            else
                rmq[k][i] = rmq[k - 1][i];

    for (int i = 0; i < q; i++)
    {
        int l, r;
        cin >> l >> r;

        int ans = INF;
        int cur = l;
        for (int k = 0; k < LOG_MAX_N; k++)
            if ((1 << k) & (r - l + 1))
            {
                ans = min(ans, rmq[k][cur]);
                cur += (1 << k);
            }
        cout << ans << endl;
    }

    return 0;
}
