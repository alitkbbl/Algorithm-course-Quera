import random


class TreapNode:
    def __init__(self, key, priority=None):
        self.key = key
        # Assign random priority if not provided
        self.priority = priority if priority is not None else random.random()
        self.left = None
        self.right = None

    def __repr__(self):
        return f"[Key:{self.key}|Prio:{self.priority:.2f}]"


class Treap:
    def __init__(self):
        self.root = None

    def _rotate_right(self, y):
        """
        Right rotation.
        Used when the left child's priority is higher than the parent.
        """
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _rotate_left(self, x):
        """
        Left rotation.
        Used when the right child's priority is higher than the parent.
        """
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def search(self, key):
        """
        Search for a key in the Treap.
        Time Complexity: O(log n) on average.
        """
        current = self.root
        while current:
            if key == current.key:
                return True  # Found
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False  # Not Found

    def insert(self, key, priority=None):
        """Public insert method."""
        if self.search(key):
            print(f"Insert skipped: Key {key} already exists.")
            return
        self.root = self._insert_recursive(self.root, key, priority)
        print(f"Inserted {key}")

    def _insert_recursive(self, node, key, priority):
        # 1. Standard BST Insert
        if node is None:
            return TreapNode(key, priority)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key, priority)
            # 2. Fix Heap property via rotation (Max-Heap on priority)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert_recursive(node.right, key, priority)
            # 2. Fix Heap property via rotation
            if node.right.priority > node.priority:
                node = self._rotate_left(node)

        return node

    def delete(self, key):
        """Public delete method."""
        if not self.search(key):
            print(f"Delete failed: Key {key} not found.")
            return
        self.root = self._delete_recursive(self.root, key)
        print(f"Deleted {key}")

    def _delete_recursive(self, node, key):
        if node is None:
            return None

        # 1. Standard BST search to find the node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node found. Now we need to delete it.

            # Case 1: Node is a leaf
            if node.left is None and node.right is None:
                return None

            # Case 2: Node has one child -> standard BST delete works,
            # but usually in Treaps we rotate down until leaf.
            # Here we handle two children by rotating the higher priority child up.

            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                # Case 3: Two children
                # Rotate the child with higher priority UP (pushing the node DOWN)
                if node.left.priority > node.right.priority:
                    node = self._rotate_right(node)
                    node.right = self._delete_recursive(node.right, key)
                else:
                    node = self._rotate_left(node)
                    node.left = self._delete_recursive(node.left, key)

        return node

    def inorder_print(self):
        """Helper to print keys in sorted order."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(f"{node.key}(p:{node.priority:.2f})")
            self._inorder(node.right, result)


# --- Example Usage ---
if __name__ == "__main__":
    print("\n--- Treap Example ---")
    treap = Treap()

    # 1. Insert Operations
    # We let priorities be random usually, but here keys are added normally.
    keys = [50, 30, 20, 40, 70, 60, 80]
    for k in keys:
        treap.insert(k)

    print("Structure (Inorder):", treap.inorder_print())

    # 2. Search Operation
    find_val = 40
    print(f"Search for {find_val}: {treap.search(find_val)}")
    print(f"Search for 99: {treap.search(99)}")

    # 3. Delete Operation
    treap.delete(20)  # Leaf (likely)
    treap.delete(50)  # Root or internal node

    print("Structure after delete:", treap.inorder_print())
