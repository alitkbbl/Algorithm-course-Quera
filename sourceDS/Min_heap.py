class MinHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def _parent(self, i):
        """Get parent index."""
        return (i - 1) // 2

    def _left_child(self, i):
        """Get left child index."""
        return 2 * i + 1

    def _right_child(self, i):
        """Get right child index."""
        return 2 * i + 2

    def _swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        """
        Move the element up to maintain the Min-Heap property.
        Used after insertion.
        """
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            parent_idx = self._parent(index)
            self._swap(index, parent_idx)
            index = parent_idx

    def _heapify_down(self, index):
        """
        Move the element down to maintain the Min-Heap property.
        Used after deletion/extraction.
        """
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)
        n = len(self.heap)

        # Compare with left child
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Compare with right child
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current node, swap and continue down
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
        print(f"Inserted {key}: Heap structure -> {self.heap}")

    def search(self, key):
        """
        Search for a key.
        Time Complexity: O(n) because heap is not sorted for searching.
        Returns the index if found, otherwise -1.
        """
        try:
            index = self.heap.index(key)
            return index
        except ValueError:
            return -1

    def get_min(self):
        """Return the minimum element (root) without removing it."""
        return self.heap[0] if self.heap else None

    def extract_min(self):
        """Remove and return the minimum element (root)."""
        if not self.heap:
            return None

        min_val = self.heap[0]
        # Replace root with the last element
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._heapify_down(0)

        print(f"Extracted Min ({min_val}): Heap structure -> {self.heap}")
        return min_val

    def delete(self, key):
        """Delete an arbitrary key from the heap."""
        index = self.search(key)
        if index == -1:
            print(f"Delete failed: Element {key} not found.")
            return False

        # Swap the element to be deleted with the last element
        last_index = len(self.heap) - 1
        self._swap(index, last_index)
        self.heap.pop()  # Remove the last element

        # If we deleted the last element directly, we are done
        if index < len(self.heap):
            # We need to restore heap property. The swapped element
            # might need to go up or down.
            parent = self._parent(index)
            if index > 0 and self.heap[index] < self.heap[parent]:
                self._heapify_up(index)
            else:
                self._heapify_down(index)

        print(f"Deleted {key}: Heap structure -> {self.heap}")
        return True


# --- Example Usage ---
if __name__ == "__main__":
    print("--- Min-Heap Example ---")
    mh = MinHeap()

    # 1. Insert Operations
    elements = [10, 4, 15, 2, 20, 1]
    for el in elements:
        mh.insert(el)

    # 2. Search Operation
    target = 15
    idx = mh.search(target)
    print(f"Search for {target}: Found at index {idx}")

    # 3. Delete Arbitrary Element
    mh.delete(15)  # Deleting a middle node
    mh.delete(100)  # Deleting non-existing node

    # 4. Extract Min
    mh.extract_min()
    print("Final Heap:", mh.heap)
