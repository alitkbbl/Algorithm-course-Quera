#include <bits/stdc++.h>

using namespace std;
#define int long long

const int MAX_N = 100010;
int a[MAX_N];
long long sum[MAX_N];

int32_t main()
{
    int n, q;
    cin >> n >> q;

    int T = sqrt(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        sum[i / T] += a[i];

    for (int i = 0; i < q; i++)
    {
        int t;
        cin >> t;
        if (t == 1)
        {
            int L, R;
            cin >> L >> R;

            long long result = 0;
            int cur = L;
            while (cur <= R)
            {
                if ((cur / T) * T == cur && cur + T <= R)
                {
                    result += sum[cur / T];
                    cur += T;
                }
                else
                {
                    result += a[cur];
                    cur++;
                }
            }
            cout << result << endl;
        }
        else
        {
            int idx, nv;
            cin >> idx >> nv;

            sum[idx / T] -= a[idx];
            a[idx] = nv;
            sum[idx / T] += a[idx];
        }
    }

    return 0;
}
