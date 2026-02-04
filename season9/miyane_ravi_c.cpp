#include <iostream>

using namespace std;

const int MAXN = 100 * 1000;

struct Heap
{
    int heap[MAXN];
    int size;

    Heap()
    {
        size = 0;
    }

    Heap(int *begin, int *end)
    {
        size = end - begin;
        for (int i = 1; i <= size; i++)
            heap[i] = *(begin + i - 1);
        for (int i = size; i > 0; i--)
            pushDown(i);
    }

    void pushDown(int v)
    {
        int minVertex = -1;
        if (2 * v <= size)
            minVertex = 2 * v;
        if (2 * v + 1 <= size && heap[2 * v] > heap[2 * v + 1])
            minVertex = 2 * v + 1;
        if (minVertex == -1 || heap[minVertex] > heap[v])
            return;
        swap(heap[v], heap[minVertex]);
        pushDown(minVertex);
    }

    void pushUp(int v)
    {
        if (v == 1 || heap[v] > heap[v / 2])
            return;
        swap(heap[v], heap[v / 2]);
        pushUp(v / 2);
    }

    void insert(int val)
    {
        size++;
        heap[size] = val;
        pushUp(size);
    }

    void deleteMin()
    {
        swap(heap[1], heap[size]);
        size--;
        pushDown(1);
    }

    int getMin()
    {
        return heap[1];
    }

    int getSize()
    {
        return size;
    }
} firstHalf, secondHalf;

int main()
{
    // We insert the negative value of all first half element
    // in "firstHalf" so that the minimum value is actually the maximum
    // We insert all the values of the second half in "secondHalf"
    int q;
    cin >> q;

    for (int currentSize = 1; currentSize <= q; currentSize++)
    {
        int x;
        cin >> x;
        if (firstHalf.getSize() == 0 || x <= -firstHalf.getMin())
            firstHalf.insert(-x);
        else
            secondHalf.insert(x);

        // in case we have to balance it:
        if (firstHalf.getSize() > (currentSize + 1) / 2)
        { // firstElements are larger than they are supposed to be:
            int x = -firstHalf.getMin();
            firstHalf.deleteMin();
            secondHalf.insert(x);
        }
        else if (secondHalf.getSize() > currentSize / 2)
        { // lastElements are larger than they are supposed to be:
            int x = secondHalf.getMin();
            secondHalf.deleteMin();
            firstHalf.insert(-x);
        }

        cout << -firstHalf.getMin() << '\n';
    }

    return 0;
}
