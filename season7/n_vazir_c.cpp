#include <iostream>
#include <vector>

using namespace std;

int kQueen(int n, int k, vector<pair<int, int>>& arr, int count, int col) {
    if (col == n) {
        return (count == k) ? 1 : 0;
    }

    int total = 0;

    // Try placing a queen in this column
    if (count < k) {
        for (int row = 0; row < n; row++) {
            bool valid = true;

            // Check if this position conflicts with existing queens
            for (const auto& queen : arr) {
                int r = queen.first;
                int c = queen.second;

                // Same row or same diagonal
                if (r == row ||
                    r + c == row + col ||
                    r - c == row - col) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                arr.push_back({row, col});
                total += kQueen(n, k, arr, count + 1, col + 1);
                arr.pop_back();
            }
        }
    }

    // Skip this column (don't place a queen here)
    total += kQueen(n, k, arr, count, col + 1);

    return total;
}

int main() {
    int n_, k_;
    cin >> n_ >> k_;

    vector<pair<int, int>> arr;
    int result = kQueen(n_, k_, arr, 0, 0);

    cout << result << endl;

    return 0;
}