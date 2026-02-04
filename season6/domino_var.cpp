#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e4 + 10, mod = 1e9 + 7;

int fib[MAXN];

int main()
{
    int n;
    cin >> n;

    fib[0] = fib[1] = 1;
    for (int i = 2; i <= n; i++)
        fib[i] = (fib[i - 1] + fib[i - 2]) % mod;

    cout << fib[n] << '\n';

    return 0;
}
