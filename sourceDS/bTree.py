class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.leaf = leaf  # True if leaf node
        self.keys = []  # List of keys
        self.children = []  # List of child pointers

    def is_full(self):
        return len(self.keys) == (2 * self.t - 1)

    def is_min(self):
        return len(self.keys) == (self.t - 1)

    def find_key(self, k):
        """Find the first key >= k"""
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        return i

    def insert_non_full(self, k):
        """Insert key into non-full node"""
        i = len(self.keys) - 1

        if self.leaf:
            # Insert into leaf node
            self.keys.append(0)
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            # Find child to insert into
            while i >= 0 and self.keys[i] > k:
                i -= 1

            i += 1

            # If child is full, split it first
            if self.children[i].is_full():
                self.split_child(i, self.children[i])

                # After split, decide which child to go to
                if self.keys[i] < k:
                    i += 1

            self.children[i].insert_non_full(k)

    def split_child(self, i, y):
        """Split child y of this node"""
        print(f"  Splitting child node with keys: {y.keys}")

        # Create new node z
        z = BTreeNode(y.t, y.leaf)

        # Move the last (t-1) keys from y to z
        z.keys = y.keys[self.t:(2 * self.t - 1)]

        # Move the last t children from y to z (if not leaf)
        if not y.leaf:
            z.children = y.children[self.t:(2 * self.t)]

        # Reduce number of keys in y
        y.keys = y.keys[0:(self.t - 1)]

        # Adjust children pointers in y
        if not y.leaf:
            y.children = y.children[0:self.t]

        # Insert median key from y into this node
        self.keys.insert(i, y.keys[self.t - 1])

        # Insert z as a new child of this node
        self.children.insert(i + 1, z)

        print(f"  After split: parent keys={self.keys}, left child={y.keys}, right child={z.keys}")

    def search(self, k):
        """Search for key k in subtree rooted with this node"""
        i = self.find_key(k)

        if i < len(self.keys) and self.keys[i] == k:
            return self, i

        if self.leaf:
            return None, -1

        return self.children[i].search(k)

    def remove(self, k):
        """Remove key k from subtree rooted with this node"""
        idx = self.find_key(k)

        # Case 1: Key is present in this node
        if idx < len(self.keys) and self.keys[idx] == k:
            if self.leaf:
                return self.remove_from_leaf(idx)
            else:
                return self.remove_from_nonleaf(idx)
        else:
            # If leaf node, key is not in tree
            if self.leaf:
                print(f"  Key {k} not found in leaf node")
                return False

            # Flag indicating if key is in last child
            flag = (idx == len(self.keys))

            # If child has less than t keys, fill it
            if self.children[idx].is_min():
                self.fill(idx)

            # Update idx after fill
            if flag and idx > len(self.keys):
                idx -= 1

            # Recur to appropriate child
            return self.children[idx].remove(k)

    def remove_from_leaf(self, idx):
        """Remove key from leaf node at index idx"""
        print(f"  Removing key {self.keys[idx]} from leaf node")
        self.keys.pop(idx)
        return True

    def remove_from_nonleaf(self, idx):
        """Remove key from non-leaf node at index idx"""
        k = self.keys[idx]
        print(f"  Removing key {k} from non-leaf node")

        # Case 2a: Left child has at least t keys
        if not self.children[idx].is_min():
            predecessor = self.get_predecessor(idx)
            self.keys[idx] = predecessor
            return self.children[idx].remove(predecessor)

        # Case 2b: Right child has at least t keys
        elif not self.children[idx + 1].is_min():
            successor = self.get_successor(idx)
            self.keys[idx] = successor
            return self.children[idx + 1].remove(successor)

        # Case 2c: Merge children
        else:
            self.merge(idx)
            return self.children[idx].remove(k)

    def get_predecessor(self, idx):
        """Find predecessor of keys[idx]"""
        current = self.children[idx]
        while not current.leaf:
            current = current.children[len(current.keys)]

        return current.keys[-1]

    def get_successor(self, idx):
        """Find successor of keys[idx]"""
        current = self.children[idx + 1]
        while not current.leaf:
            current = current.children[0]

        return current.keys[0]

    def fill(self, idx):
        """Fill child at idx which has less than t-1 keys"""
        print(f"  Filling child at index {idx} with keys: {self.children[idx].keys}")

        # Borrow from left sibling
        if idx != 0 and not self.children[idx - 1].is_min():
            self.borrow_from_left(idx)

        # Borrow from right sibling
        elif idx != len(self.keys) and not self.children[idx + 1].is_min():
            self.borrow_from_right(idx)

        # Merge with sibling
        else:
            if idx != len(self.keys):
                self.merge(idx)
            else:
                self.merge(idx - 1)

    def borrow_from_left(self, idx):
        """Borrow a key from left sibling"""
        print(f"  Borrowing from left sibling")
        child = self.children[idx]
        sibling = self.children[idx - 1]

        # Move a key from parent to child
        child.keys.insert(0, self.keys[idx - 1])

        # Move last key from sibling to parent
        self.keys[idx - 1] = sibling.keys.pop()

        # Move last child from sibling to child
        if not sibling.leaf:
            child.children.insert(0, sibling.children.pop())

    def borrow_from_right(self, idx):
        """Borrow a key from right sibling"""
        print(f"  Borrowing from right sibling")
        child = self.children[idx]
        sibling = self.children[idx + 1]

        # Move a key from parent to child
        child.keys.append(self.keys[idx])

        # Move first key from sibling to parent
        self.keys[idx] = sibling.keys.pop(0)

        # Move first child from sibling to child
        if not sibling.leaf:
            child.children.append(sibling.children.pop(0))

    def merge(self, idx):
        """Merge child[idx] with child[idx+1]"""
        print(f"  Merging child {idx} and child {idx + 1}")
        child = self.children[idx]
        sibling = self.children[idx + 1]

        # Move key from parent to child
        child.keys.append(self.keys[idx])

        # Copy keys from sibling to child
        child.keys.extend(sibling.keys)

        # Copy children from sibling to child
        if not child.leaf:
            child.children.extend(sibling.children)

        # Remove key from parent
        self.keys.pop(idx)

        # Remove sibling from parent
        self.children.pop(idx + 1)


class BTree:
    def __init__(self, t):
        self.t = t  # Minimum degree
        self.root = None

    def search(self, k):
        """Search for key k in the tree"""
        print(f"\n{'=' * 50}")
        print(f"SEARCHING FOR KEY {k}")
        print(f"{'=' * 50}")

        if self.root is None:
            print("Tree is empty")
            return False

        node, idx = self.root.search(k)

        if node:
            print(f"✓ Key {k} FOUND at index {idx} in node with keys: {node.keys}")
            return True
        else:
            print(f"✗ Key {k} NOT FOUND in the tree")
            return False

    def insert(self, k):
        """Insert key k into the tree"""
        print(f"\n{'=' * 50}")
        print(f"INSERTING KEY {k}")
        print(f"{'=' * 50}")

        if self.root is None:
            print(f"Tree is empty. Creating root with key {k}")
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(k)
        else:
            print(f"Root keys: {self.root.keys}")

            # If root is full, split it
            if self.root.is_full():
                print(f"Root is full (keys: {self.root.keys}), splitting root")
                s = BTreeNode(self.t, False)
                s.children.append(self.root)
                s.split_child(0, self.root)

                # Decide which child to insert into
                i = 0
                if s.keys[0] < k:
                    i = 1

                s.children[i].insert_non_full(k)
                self.root = s
            else:
                self.root.insert_non_full(k)

        self.print_tree()

    def delete(self, k):
        """Delete key k from the tree"""
        print(f"\n{'=' * 50}")
        print(f"DELETING KEY {k}")
        print(f"{'=' * 50}")

        if self.root is None:
            print("Tree is empty, nothing to delete")
            return

        print(f"Starting deletion from root with keys: {self.root.keys}")
        removed = self.root.remove(k)

        # If root becomes empty after deletion
        if len(self.root.keys) == 0:
            if self.root.leaf:
                print("Root is now empty, tree is empty")
                self.root = None
            else:
                print("Root has no keys but has children, promoting first child to root")
                self.root = self.root.children[0]

        if removed:
            print(f"✓ Key {k} successfully deleted")
        else:
            print(f"✗ Key {k} not found for deletion")

        if self.root:
            self.print_tree()

    def inorder_traversal(self, node=None, result=None):
        """Inorder traversal of the tree"""
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is None:
            return result

        # Traverse all children and keys
        for i in range(len(node.keys)):
            if not node.leaf:
                self.inorder_traversal(node.children[i], result)
            result.append(node.keys[i])

        if not node.leaf:
            self.inorder_traversal(node.children[len(node.keys)], result)

        return result

    def level_order_traversal(self):
        """Level-order traversal of the tree"""
        if self.root is None:
            return []

        result = []
        queue = [(self.root, 0)]

        while queue:
            node, level = queue.pop(0)

            if len(result) <= level:
                result.append([])

            result[level].append(node.keys)

            if not node.leaf:
                for child in node.children:
                    queue.append((child, level + 1))

        return result

    def print_tree(self, node=None, level=0, child_num="Root"):
        """Print tree structure"""
        if node is None:
            node = self.root

        if node is None:
            print("Tree is empty")
            return

        indent = "    " * level
        prefix = f"{child_num}: "

        # Print node keys
        keys_str = "[" + ", ".join(map(str, node.keys)) + "]"
        print(f"{indent}{prefix}{keys_str} {'(leaf)' if node.leaf else ''}")

        # Print children
        if not node.leaf:
            for i, child in enumerate(node.children):
                self.print_tree(child, level + 1, f"Child-{i}")

    def print_tree_visual(self):
        """Visual tree representation"""
        print("\nVISUAL TREE REPRESENTATION:")
        print("-" * 40)

        if self.root is None:
            print("Tree is empty")
            return

        levels = self.level_order_traversal()
        for level, nodes in enumerate(levels):
            print(f"Level {level}: ", end="")
            for i, keys in enumerate(nodes):
                print(f"[{', '.join(map(str, keys))}]", end="  ")
            print()


# Test B-Tree
if __name__ == "__main__":
    # Create B-Tree with minimum degree 3 (order 5)
    t = 3
    btree = BTree(t)

    print("B-TREE DEMONSTRATION (Minimum degree = 3)")
    print("=" * 60)

    # Insert values
    print("\nPHASE 1: INSERTING KEYS")
    print("-" * 60)

    keys = [40, 20, 60, 10, 30, 50, 70, 25, 27, 26, 5, 15, 65, 80, 75]

    for i, key in enumerate(keys):
        btree.insert(key)
        print(f"\nStep {i + 1} Summary:")
        print(f"Inorder traversal: {btree.inorder_traversal()}")
        print("-" * 40)

    # Search for some keys
    print("\nPHASE 2: SEARCHING KEYS")
    print("-" * 60)

    search_keys = [40, 25, 100, 75, 5]

    for key in search_keys:
        btree.search(key)

    # Tree information
    print("\nPHASE 3: TREE INFORMATION")
    print("-" * 60)

    print(f"Inorder traversal (sorted): {btree.inorder_traversal()}")
    print(f"Level-order traversal: {btree.level_order_traversal()}")
    btree.print_tree_visual()

    # Delete values
    print("\nPHASE 4: DELETING KEYS")
    print("-" * 60)

    delete_keys = [60, 70, 40, 25, 20]

    for i, key in enumerate(delete_keys):
        btree.delete(key)
        print(f"\nAfter deletion {i + 1}:")
        print(f"Inorder traversal: {btree.inorder_traversal()}")
        print("-" * 40)

    # Final tree information
    print("\nFINAL TREE INFORMATION")
    print("=" * 60)

    print(f"Root: {btree.root.keys if btree.root else 'None'}")
    print(f"Final inorder traversal: {btree.inorder_traversal()}")
    print(f"Final level-order traversal: {btree.level_order_traversal()}")

    print("\nFINAL TREE STRUCTURE:")
    print("-" * 40)
    btree.print_tree()

    print("\nFINAL VISUAL REPRESENTATION:")
    btree.print_tree_visual()