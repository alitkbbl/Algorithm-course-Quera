#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

void solve() {
    string line;

    // Read T
    if (!getline(cin, line) || line.empty()) {
        return;
    }

    int T;
    try {
        T = stoi(line);
    } catch (...) {
        return;
    }

    for (int t = 0; t < T; t++) {
        // Read n and K
        if (!getline(cin, line) || line.empty()) {
            break;
        }

        stringstream ss(line);
        int n, K;
        if (!(ss >> n >> K)) {
            break;
        }

        // Read array A
        if (!getline(cin, line) || line.empty()) {
            break;
        }

        stringstream ss2(line);
        vector<int> A(n);
        bool valid = true;
        for (int i = 0; i < n; i++) {
            if (!(ss2 >> A[i])) {
                valid = false;
                break;
            }
        }

        if (!valid) {
            break;
        }

        // Calculate prefix sums
        vector<long long> ps(n + 1);
        ps[0] = 0;
        long long current_sum = 0;
        for (int i = 0; i < n; i++) {
            current_sum += A[i];
            ps[i + 1] = current_sum;
        }

        // Sort prefix sums
        sort(ps.begin(), ps.end());

        long long answer = 0;
        int m = ps.size();

        for (long long x : ps) {
            int left_count = lower_bound(ps.begin(), ps.end(), x - K) - ps.begin();

\
            int right_idx = upper_bound(ps.begin(), ps.end(), x + K) - ps.begin();
            int right_count = m - right_idx;

            answer += (left_count + right_count);
        }

        cout << answer / 2 << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}