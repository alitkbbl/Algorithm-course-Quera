#include <iostream>
#include <vector>

using namespace std;

vector<int> mergeTwoArrays(const vector<int>& arr1, const vector<int>& arr2) {
    vector<int> result;
    int p1 = 0, p2 = 0;

    while (p1 < arr1.size() && p2 < arr2.size()) {
        if (arr1[p1] < arr2[p2]) {
            result.push_back(arr1[p1]);
            p1++;
        } else {
            result.push_back(arr2[p2]);
            p2++;
        }
    }

    // Add remaining elements from arr1
    while (p1 < arr1.size()) {
        result.push_back(arr1[p1]);
        p1++;
    }

    // Add remaining elements from arr2
    while (p2 < arr2.size()) {
        result.push_back(arr2[p2]);
        p2++;
    }

    return result;
}

vector<int> mergeKArrays(const vector<vector<int>>& arrays) {
    if (arrays.size() == 1) {
        return arrays[0];
    }

    int mid = arrays.size() / 2;

    // Split arrays into left and right halves
    vector<vector<int>> left(arrays.begin(), arrays.begin() + mid);
    vector<vector<int>> right(arrays.begin() + mid, arrays.end());

    // Recursively merge left and right halves
    vector<int> leftMerged = mergeKArrays(left);
    vector<int> rightMerged = mergeKArrays(right);

    // Merge the two merged halves
    return mergeTwoArrays(leftMerged, rightMerged);
}

int main() {
    int k, n;
    cin >> k >> n;

    vector<vector<int>> arrays(n);

    // Read arrays
    for (int i = 0; i < n; i++) {
        arrays[i].resize(k);
        for (int j = 0; j < k; j++) {
            cin >> arrays[i][j];
        }
    }

    // Merge all arrays
    vector<int> result = mergeKArrays(arrays);

    // Print result
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i != result.size() - 1) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}