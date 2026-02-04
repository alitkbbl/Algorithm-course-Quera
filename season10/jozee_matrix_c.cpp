#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 510;
int m[MAX_N][MAX_N];
long long par[MAX_N][MAX_N]; // par[i] <= 1000000 * 1000000 so it's should be long long

int main()
{
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> m[i][j];

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            par[i][j] = m[i - 1][j - 1] + par[i - 1][j] + par[i][j - 1] - par[i - 1][j - 1];

    for (int i = 0; i < q; i++)
    {
        int x, y, X, Y;
        cin >> x >> y >> X >> Y;

        cout << par[X + 1][Y + 1] - par[X + 1][y] - par[x][Y + 1] + par[x][y] << '\n';
    }

    return 0;
}
