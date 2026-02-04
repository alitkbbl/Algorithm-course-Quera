#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAXN = 200000 + 1;

ll a[MAXN], ps[MAXN];


int binary_search(int l, int r, ll V)
{
    if (r - l <= 0)
        return r; // interval has zero length
    if (r - l == 1)
    {
        if (ps[l] >= V)
            return l; // if ps[l] >= V then l
        else
            return r; // else r
    }
    int mid = (l + r) / 2;
    if (ps[mid] >= V)
        return binary_search(l, mid, V); // search in left part
    else
        return binary_search(mid, r, V); // search in right part
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(0);

    int T;
    cin >> T;

    while (T--)
    {
        int n;
        ll K;
        cin >> n >> K;

        ll ans = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            ps[i + 1] = ps[i] + a[i]; // compute ps[i] as described.
        }

        sort(ps, ps + n + 1); // sort ps.

        for (int i = 0; i <= n; i++)
        {
            int lb = binary_search(0, n + 1, ps[i] - K);     // find the first index bigger or equal to ps[i] - K
            int rb = binary_search(0, n + 1, ps[i] + K + 1); // find the first index bigger than ps[i] + K
            ans += n + 1 - (rb - lb); //(n + 1) - (rb - lb) is good pairs with ps[i].
        }
        cout << ans / 2 << '\n'; // each pair counted twice.
    }

    return 0;
}
