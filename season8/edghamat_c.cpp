#include <bits/stdc++.h>
using namespace std;

const int MAXN = 5e6 + 10;
int n, k, td = 0;

int a[MAXN], b[MAXN];

void solve(int l, int r)
{ // will merge arrays [l, r) and sorted order is in [l*n, r*n);
    if (r - l <= 1)
        return; // array is sorted by default
    int mid = (l + r) / 2;

    solve(l, mid); // sort left part
    solve(mid, r); // sort right part

    int p1 = l * n, p2 = mid * n, cnt = 0;

    // merge two sorted parts and sort [l*n, r*n)
    while (p1 < mid * n || p2 < r * n)
    {
        if (p1 == mid * n)
            b[cnt++] = a[p2++];
        else if (p2 == r * n)
            b[cnt++] = a[p1++];
        else if (a[p1] < a[p2])
            b[cnt++] = a[p1++];
        else
            b[cnt++] = a[p2++];
    }

    for (int i = 0; i < (r - l) * n; i++)
        a[i + l * n] = b[i];
}

int main()
{
    cin >> n >> k;

    // input data.
    for (int i = 0; i < k; i++)
        for (int j = 0; j < n; j++)
            cin >> a[td], td++;

    // sort arrays [0, k)
    solve(0, k);

    for (int i = 0; i < n * k; i++)
        cout << a[i] << ' ';
    cout << endl;

    return 0;
}
