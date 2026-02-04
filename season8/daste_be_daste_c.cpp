#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second

typedef long long ll;

const int MAXN = 17, MAXL = (1 << MAXN);

int a[MAXL];

// will return a pair which first element is maximum prize in sub array [l, r)
//  and second element is equal to maximum in sub array [l, r)
pair<ll, ll> f(int l, int r)
{
    if (r - l == 1)
        return make_pair(a[l], a[l]);

    int mid = (l + r) / 2;
    pair<ll, ll> X = f(l, mid);
    pair<ll, ll> Y = f(mid, r);

    pair<ll, ll> res;

    // maximum of sub array [l, r) equals to maximum of max[l, mid), max[mid, r)
    res.S = max(X.S, Y.S);

    // if we go to left part prize is prize[l, mid) + max[mid, r)
    // else prize is prize[mid, r) + max[l, mid)

    res.F = max(X.F + Y.S, Y.F + X.S);
    return res;
}

int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0);

    int n;
    cin >> n;
    int l = (1 << n);

    for (int i = 0; i < l; i++)
        cin >> a[i];
    pair<ll, ll> X = f(0, l);

    cout << X.F << '\n';

    return 0;
}
