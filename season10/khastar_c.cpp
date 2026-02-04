#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 2010;
vector<int> v[MAX_N];

int main()
{
    int n, q;
    cin >> n >> q;

    for (int i = 1; i <= n; i++)
        v[i].push_back(i);

    for (int i = 0; i < q; i++)
    {
        int queryType;
        cin >> queryType;

        if (queryType == 1)
        {
            int a, b;
            cin >> a >> b;

            if (min(a, b) > 0 && max(a, b) <= n)
            {
                for (int x : v[a])
                    v[b].push_back(x);
                v[a].clear();
            }
        }
        else if (queryType == 2)
        {
            int c;
            cin >> c;

            if (c > 0 && c <= n)
                cout << v[c].size() << '\n';
        }
        else
        {
            int d;
            cin >> d;

            if (d > 0 && d <= n)
            {
                sort(v[d].begin(), v[d].end());
                if (v[d].empty())
                    cout << -1 << '\n';
                else
                {
                    for (int x : v[d])
                        cout << x << ' ';
                    cout << '\n';
                }
            }
        }
    }

    return 0;
}
