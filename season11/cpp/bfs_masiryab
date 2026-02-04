#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 * 1000 + 10, INF = 1000 * 1000 * 1000;

vector<int> adj[MAXN];
int dis[MAXN];
int parent[MAXN];
queue<int> q;

void BFS(int n, int r)
{
    for (int i = 1; i <= n; i++)
        dis[i] = INF;

    dis[r] = 0;
    q.push(r);
    parent[r] = r;

    while (!q.empty())
    {
        int v = q.front();
        q.pop();
        for (auto u : adj[v])
        {
            if (dis[u] > dis[v] + 1)
            {
                dis[u] = dis[v] + 1;
                q.push(u);
                parent[u] = v;
            }
        }
    }
}

int main()
{
    int n, m, s, t;
    cin >> n >> m >> s >> t;

    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    BFS(n, s);

    if (parent[t] == 0)
    {
        cout << -1;
        return 0;
    }

    cout << dis[t] << '\n';

    vector<int> ans;
    while (t != parent[t])
    {
        ans.push_back(t);
        t = parent[t];
    }
    ans.push_back(s);

    for (int i = ans.size() - 1; i >= 0; i--)
        cout << ans[i] << ' ';

    return 0;
}
