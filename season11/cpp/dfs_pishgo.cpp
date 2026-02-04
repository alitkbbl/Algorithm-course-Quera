#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000 + 5;
vector<int> vertex[MAXN];
bool mark[MAXN];

void dfs(int x)
{
    mark[x] = true;
    for (int neighbor : vertex[x])
        if (!mark[neighbor])
            dfs(neighbor);
}

int main()
{
    int n, m;
    cin >> n >> m;

    int s, t;
    cin >> s >> t;

    s--, t--;

    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        vertex[u].push_back(v);
        vertex[v].push_back(u);
    }

    dfs(s);

    if (mark[t])
        cout << "YES";
    else
        cout << "NO";

    return 0;
}
