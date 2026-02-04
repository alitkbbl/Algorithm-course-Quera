#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1000 + 10;

int x[MAXN], y[MAXN], n;
bool mark[MAXN];

// make a graph which vertexes correspond to each island
// vertexes u, v are connected if and only if x[i] == x[j] || y[i] == y[j].
// now we want to compute number of connected components in this graph.
// and then we can add number of connected components minus one connections to make the graph connected.

void DFS(int v)
{
    mark[v] = true;
    for (int u = 0; u < n; u++)
        if ((x[v] == x[u] || y[v] == y[u]) && !mark[u])
            DFS(u);
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> x[i] >> y[i];

    int ans = -1;
    for (int i = 0; i < n; i++)
    {
        if (mark[i])
            continue;
        ans++;
        DFS(i);
    }

    cout << ans << endl;
}
