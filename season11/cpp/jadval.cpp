#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1010;

int a[MAXN][MAXN], n, cnt, id[MAXN][MAXN];
// id[i][j] is number of component of (i, j)
// cnt is number of connected components.
// a component is block as described in task.

bool f1[MAXN * MAXN], f2[MAXN * MAXN];
// f2[i] is false if and only if component i is "darre".
// f1[i] is false if and only if component i is "gholle"

const int dx[8] = {1, -1, 0, 0, 1, 1, -1, -1}, dy[8] = {0, 0, 1, -1, 1, -1, 1, -1};

// find connected components
void DFS(int x, int y)
{
    id[x][y] = cnt;
    // this for will iterate over neighbors of (x, y)
    for (int i = 0; i < 8; i++)
    {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= n)
            continue;
        if (a[nx][ny] == a[x][y] && id[nx][ny] == -1)
            DFS(nx, ny);
    }
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> a[i][j];

    memset(id, -1, sizeof id); // will fill all id[i][j] with -1

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (id[i][j] != -1)
                continue;
            DFS(i, j);
            cnt++;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int c = id[i][j];
            // this for will iterate over neighbors of (i, j)
            for (int k = 0; k < 8; k++)
            {
                int nx = i + dx[k], ny = j + dy[k];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                    continue;

                //(nx, ny) is neighbor of (i, j).
                if (id[nx][ny] != id[i][j])
                {
                    if (a[nx][ny] < a[i][j])
                        f1[id[i][j]] = true; // component of (i, j) cannot be "darre"
                    else
                        f2[id[i][j]] = true; // component of (i, j) cannot be "gholle"
                }
            }
        }
    }

    int ans1 = 0, ans2 = 0;
    for (int i = 0; i < cnt; i++)
    {
        if (!f2[i])
            ans1++; // add number of "gholle"
        if (!f1[i])
            ans2++; // add number of "darre"
    }

    cout << ans1 << ' ' << ans2 << endl;

    return 0;
}
