from collections import deque


class Node:
    """
    Represents a single node in the Heap.
    Each node stores a value and references to its parent and children.
    """

    def __init__(self, value):
        self.value = value
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.parent = None  # Pointer to the parent node

    def __repr__(self):
        return f"Node({self.value})"


class MinHeap:
    """
    A Min-Heap implementation using a Node-based tree structure
    (not a list/array).
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        """Checks if the heap is empty."""
        return self.root is None

    def peek(self):
        """Returns the minimum element (root) without removing it."""
        if self.is_empty():
            return None
        return self.root.value

    def insert(self, value):
        """
        Inserts a new value into the heap.
        1. Finds the first available spot in level-order.
        2. Adds the node.
        3. Bubbles up (heapifies up) to restore heap property.
        """
        new_node = Node(value)

        # Case 1: Heap is empty, make new node the root
        if self.root is None:
            self.root = new_node
            self.size += 1
            return

        # Case 2: Find the first node that has an empty child slot (Level Order)
        # We use a Queue to perform Breadth-First Search (BFS)
        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            # Check left child
            if current.left is None:
                current.left = new_node
                new_node.parent = current
                break
            else:
                queue.append(current.left)

            # Check right child
            if current.right is None:
                current.right = new_node
                new_node.parent = current
                break
            else:
                queue.append(current.right)

        self.size += 1
        # Restore min-heap property by bubbling up
        self._heapify_up(new_node)

    def extract_min(self):
        """
        Removes and returns the minimum element (root).
        1. Swaps root value with the last inserted node's value.
        2. Deletes the last node.
        3. Bubbles down (heapifies down) from root to restore heap property.
        """
        if self.is_empty():
            return None

        min_val = self.root.value

        # Case 1: Only one node exists
        if self.size == 1:
            self.root = None
            self.size = 0
            return min_val

        # Case 2: More than one node
        # Find the last node in the tree (the rightmost node on the lowest level)
        last_node = self._get_last_node()

        # Swap values: Move last node's value to root
        # Note: Swapping values is easier than rewiring pointers
        self.root.value = last_node.value

        # Remove the last node from the tree
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        self.size -= 1

        # Restore min-heap property by bubbling down from root
        self._heapify_down(self.root)

        return min_val

    def _heapify_up(self, node):
        """
        Moves the node up the tree as long as it is smaller than its parent.
        """
        while node.parent and node.value < node.parent.value:
            # Swap values between node and parent
            node.value, node.parent.value = node.parent.value, node.value
            # Move pointer up
            node = node.parent

    def _heapify_down(self, node):
        """
        Moves the node down the tree as long as it is larger than its children.
        Always swaps with the smaller of the two children.
        """
        while node:
            smallest = node
            left_child = node.left
            right_child = node.right

            # Compare with left child
            if left_child and left_child.value < smallest.value:
                smallest = left_child

            # Compare with right child
            if right_child and right_child.value < smallest.value:
                smallest = right_child

            # If the smallest is still the current node, we are done
            if smallest == node:
                break

            # Swap values with the smallest child
            node.value, smallest.value = smallest.value, node.value

            # Move pointer down to continue
            node = smallest

    def _get_last_node(self):
        """
        Helper method to find the last node in the tree (level-order).
        This is required for the extract_min operation.
        """
        if not self.root:
            return None

        queue = deque([self.root])
        last_node = None

        while queue:
            last_node = queue.popleft()
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        return last_node

    def print_heap(self):
        """
        Helper to print the heap structure (Level Order).
        """
        if not self.root:
            print("Heap is empty")
            return

        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(str(node.value))
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        print("Heap (Level Order):", " -> ".join(result))


# --- Usage Example ---

if __name__ == "__main__":
    heap = MinHeap()

    print("Inserting: 10, 5, 20, 2, 8")
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(2)  # This should bubble up to become root
    heap.insert(8)

    heap.print_heap()
    # Expected output should start with 2

    print(f"Minimum value: {heap.peek()}")

    print("\nExtracting minimums...")
    print(f"Extracted: {heap.extract_min()}")
    heap.print_heap()

    print(f"Extracted: {heap.extract_min()}")
    heap.print_heap()
