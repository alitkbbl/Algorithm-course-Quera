#include <bits/stdc++.h>
using namespace std;

int main()
{
    int W, H, q;
    cin >> W >> H >> q;

    set<int> vertical; // set of vertical cuts initially with cuts "0" and "W"
    vertical.insert(0), vertical.insert(W);
    set<int> horizontal; // set of horizontal cuts initially with cuts "0" and "H"
    horizontal.insert(0), horizontal.insert(H);

    multiset<int> vCuts; // set of vertical piece sizes
    vCuts.insert(W);
    multiset<int> hCuts; // set of horizontal piece sizes
    hCuts.insert(H);

    for (int i = 0; i < q; i++)
    {
        char typeOfCut;
        int x;
        cin >> typeOfCut >> x;

        if (typeOfCut == 'H')
        {
            set<int>::iterator nextCut = horizontal.lower_bound(x);
            set<int>::iterator prevCut = nextCut;
            prevCut--;
            hCuts.erase(hCuts.find(*nextCut - *prevCut));
            hCuts.insert(x - *prevCut);
            hCuts.insert(*nextCut - x);
            horizontal.insert(x);
        }
        else
        {
            set<int>::iterator nextCut = vertical.lower_bound(x);
            set<int>::iterator prevCut = nextCut;
            prevCut--;
            vCuts.erase(vCuts.find(*nextCut - *prevCut));
            vCuts.insert(x - *prevCut);
            vCuts.insert(*nextCut - x);
            vertical.insert(x);
        }

        cout << 1ll * *(--hCuts.end()) * *(--vCuts.end()) << '\n';
    }

    return 0;
}
