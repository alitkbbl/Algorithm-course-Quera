#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 100010;  // Maximum size of the array
int a[MAX_N];              // Original array to store elements
int block_max[MAX_N];      // Array to store maximum of each block

int main() {
    int n, q;
    cin >> n >> q;
    int block_size = sqrt(n);  // Determine block size (approximately sqrt(n))

    for (int i = 0; i < n; i++)
        cin >> a[i];

    // Calculate maximum for each block
    for (int i = 0; i < n; i++)
        // block_max[x] stores max of block x
        // (from a[x*block_size] to a[(x+1)*block_size-1])
        block_max[i / block_size] = max(block_max[i / block_size], a[i]);

    // Process each query
    for (int i = 0; i < q; i++) {
        int query_type;
        cin >> query_type;

        if (query_type == 1) {  // Range maximum query
            int L, R;
            cin >> L >> R;

            int result = 0;
            int current = L;

            while (current <= R) {
                // Check if we can take a whole block
                if (current % block_size == 0 && current + block_size <= R) {
                    result = max(result, block_max[current / block_size]);
                    current += block_size;
                } else {  // Otherwise process element by element
                    result = max(result, a[current]);
                    current++;
                }
            }
            cout << result << endl;
        } else {  // Update query
            int index, new_value;
            cin >> index >> new_value;

            // Update the original array
            a[index] = new_value;

            // Recalculate the maximum for the affected block
            int block_num = index / block_size;
            block_max[block_num] = 0;  // Reset before recalculation
            int block_start = block_num * block_size;
            int block_end = (block_num + 1) * block_size;
            for (int i = block_start; i < block_end; i++)
                block_max[block_num] = max(block_max[block_num], a[i]);
        }
    }

    return 0;
}