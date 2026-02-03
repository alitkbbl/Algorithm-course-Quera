#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int q, k;
    if (!(cin >> q >> k)) return 0;

    set<int> landed_planes;

    while (q--) {
        int x;
        cin >> x;

        auto it = landed_planes.lower_bound(x);

        bool permission = true;

        if (it != landed_planes.end()) {
            if (*it - x < k) {
                permission = false;
            }
        }

        if (permission && it != landed_planes.begin()) {
            auto left_it = prev(it);
            if (x - *left_it < k) {
                permission = false;
            }
        }

        if (permission) {
            cout << "Permission Granted!\n";
            landed_planes.insert(x);
        } else {
            cout << "Permission Denied!\n";
        }
    }

    return 0;
}
