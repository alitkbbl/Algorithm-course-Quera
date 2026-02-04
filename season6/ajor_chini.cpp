#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll mod = 1e9 + 7;
int MAXN = 1e5 + 1;

int32_t main()
{
    vector<ll> f(MAXN);

    f[0] = f[1] = f[2] = 1;
    f[3] = 2;
    for (int i = 4; i < MAXN; i++)
        f[i] = (f[i - 1] + f[i - 2] + f[i - 3] - f[i - 4] + mod) % mod;

    int q;
    cin >> q;
    while (q--)
    {
        ll x;
        cin >> x;
        cout << f[x] << '\n';
    }

    return 0;
}
