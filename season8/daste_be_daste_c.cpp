#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int n;
    if (!(cin >> n)) {
        return 0;
    }

    int num_teams = 1 << n;
    vector<int> p(num_teams);

    for (int i = 0; i < num_teams; i++) {
        cin >> p[i];
    }

    // Using iterative approach instead of recursion to avoid stack overflow
    // This processes the tournament bottom-up
    vector<int> max_vals = p;
    vector<int> prizes = p;

    int size = num_teams;
    while (size > 1) {
        int new_size = size / 2;
        vector<int> new_max(new_size);
        vector<int> new_prize(new_size);

        for (int i = 0; i < new_size; i++) {
            int left_idx = i * 2;
            int right_idx = i * 2 + 1;

            // Current maximum in this subtree
            new_max[i] = max(max_vals[left_idx], max_vals[right_idx]);

            // Calculate prize
            int option1 = prizes[left_idx] + max_vals[right_idx];
            int option2 = prizes[right_idx] + max_vals[left_idx];
            new_prize[i] = max(option1, option2);
        }

        max_vals = move(new_max);
        prizes = move(new_prize);
        size = new_size;
    }

    cout << prizes[0] << endl;

    return 0;
}