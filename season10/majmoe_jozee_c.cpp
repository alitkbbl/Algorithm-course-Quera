#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 1000010;
int a[MAX_N];
long long par[MAX_N]; // par[i] <= 1000000 * 1000000 so it's should be long long

int main()
{
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n; i++)
        cin >> a[i];

    par[0] = 0;
    for (int i = 1; i <= n; i++)
        par[i] = par[i - 1] + a[i - 1];

    for (int i = 0; i < q; i++)
    {
        int l, r;
        cin >> l >> r;
        cout << par[r + 1] - par[l] << '\n';
    }

    return 0;
}
