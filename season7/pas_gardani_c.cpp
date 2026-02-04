#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

vector<vector<int>> sequences;
const int MAX_NUM = 1000000;
bool mark[MAX_NUM + 1];
int n;

long long backtrack(int r) {
    if (r == n) {
        return 1;
    }

    long long total = 0;

    for (int x : sequences[r]) {
        if (!mark[x]) {
            mark[x] = true;
            total += backtrack(r + 1);
            mark[x] = false;
        }
    }

    return total;
}

int main() {
    cin >> n;

    sequences.resize(n);

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        sequences[i].resize(k);
        for (int j = 0; j < k; j++) {
            cin >> sequences[i][j];
        }
    }

    memset(mark, false, sizeof(mark));

    long long answer = backtrack(0);

    cout << answer << endl;

    return 0;
}