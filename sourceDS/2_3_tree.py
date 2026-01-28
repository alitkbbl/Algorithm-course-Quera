class Node23:
    def __init__(self, keys=None, children=None, is_leaf=True):
        self.keys = keys if keys is not None else []
        self.children = children if children is not None else []
        self.is_leaf = is_leaf
        self.parent = None

    def is_full(self):
        return len(self.keys) == 3

    def is_2node(self):
        return len(self.keys) == 1

    def is_3node(self):
        return len(self.keys) == 2

    def insert_key(self, key):
        """Insert key into node in sorted order"""
        self.keys.append(key)
        self.keys.sort()

    def remove_key(self, key):
        """Remove key from node"""
        if key in self.keys:
            self.keys.remove(key)
            return True
        return False

    def get_child_for_key(self, key):
        """Find appropriate child for given key"""
        if self.is_leaf:
            return None

        for i, k in enumerate(self.keys):
            if key < k:
                return self.children[i]
        return self.children[-1]


class TwoThreeTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert new key"""
        print(f"\n{'=' * 50}")
        print(f"Inserting key {key}")
        print(f"{'=' * 50}")

        if self.root is None:
            self.root = Node23([key])
            print("Tree was empty. Created new root.")
            self.print_tree()
            return

        # Find leaf node for insertion
        node = self._find_leaf(self.root, key)

        # Insert into leaf node
        node.insert_key(key)

        # If node is overfull, split it
        if len(node.keys) == 3:
            self._split_node(node)

        print(f"After inserting {key}:")
        self.print_tree()

    def _find_leaf(self, node, key):
        """Find appropriate leaf node for key insertion"""
        if node.is_leaf:
            return node

        # Find appropriate child
        for i, k in enumerate(node.keys):
            if key < k:
                return self._find_leaf(node.children[i], key)
        return self._find_leaf(node.children[-1], key)

    def _split_node(self, node):
        """Split an overfull node"""
        if not node.is_full():
            return

        # Middle key to promote to parent
        middle_key = node.keys[1]

        # Create two new nodes
        left_node = Node23([node.keys[0]], [], node.is_leaf)
        right_node = Node23([node.keys[2]], [], node.is_leaf)

        # If node is not leaf, also split children
        if not node.is_leaf:
            left_node.children = node.children[:2]
            right_node.children = node.children[2:]
            left_node.is_leaf = False
            right_node.is_leaf = False

            # Set parent for children
            for child in left_node.children:
                child.parent = left_node
            for child in right_node.children:
                child.parent = right_node

        # If node is root
        if node.parent is None:
            new_root = Node23([middle_key], [left_node, right_node], False)
            left_node.parent = new_root
            right_node.parent = new_root
            self.root = new_root
            return

        # If node is not root
        parent = node.parent
        parent.insert_key(middle_key)

        # Replace old node with two new nodes
        index = parent.children.index(node)
        parent.children.pop(index)
        parent.children.insert(index, right_node)
        parent.children.insert(index, left_node)

        left_node.parent = parent
        right_node.parent = parent

        # If parent is full, split it too
        if parent.is_full():
            self._split_node(parent)

    def delete(self, key):
        """Delete a key"""
        print(f"\n{'=' * 50}")
        print(f"Deleting key {key}")
        print(f"{'=' * 50}")

        node = self._find_node(self.root, key)
        if node is None:
            print(f"Key {key} not found!")
            return

        if node.is_leaf:
            self._delete_from_leaf(node, key)
        else:
            # Find successor (rightmost node in left subtree)
            successor = self._find_successor(node, key)
            # Replace key with successor
            key_index = node.keys.index(key)
            node.keys[key_index] = successor.keys[0]
            # Delete successor from leaf
            self._delete_from_leaf(successor, successor.keys[0])

        print(f"After deleting {key}:")
        self.print_tree()

    def _find_node(self, node, key):
        """Find node containing the key"""
        if node is None:
            return None

        if key in node.keys:
            return node

        if node.is_leaf:
            return None

        # Find appropriate child
        for i, k in enumerate(node.keys):
            if key < k:
                return self._find_node(node.children[i], key)
        return self._find_node(node.children[-1], key)

    def _find_successor(self, node, key):
        """Find successor for a key"""
        key_index = node.keys.index(key)
        current = node.children[key_index + 1]
        while not current.is_leaf:
            current = current.children[0]
        return current

    def _delete_from_leaf(self, node, key):
        """Delete key from leaf node"""
        if not node.remove_key(key):
            return

        # If node is root and became empty
        if node == self.root and not node.keys:
            self.root = None
            return

        # If leaf node has too few keys, fix it
        if len(node.keys) < 1 and node != self.root:
            self._fix_leaf(node)

    def _fix_leaf(self, node):
        """Fix a leaf node with too few keys"""
        parent = node.parent
        node_index = parent.children.index(node)

        # Try to borrow from left sibling
        if node_index > 0:
            left_sibling = parent.children[node_index - 1]
            if len(left_sibling.keys) > 1:
                self._borrow_from_left(node, parent, node_index)
                return

        # Try to borrow from right sibling
        if node_index < len(parent.children) - 1:
            right_sibling = parent.children[node_index + 1]
            if len(right_sibling.keys) > 1:
                self._borrow_from_right(node, parent, node_index)
                return

        # If can't borrow, merge
        if node_index > 0:
            # Merge with left sibling
            self._merge_with_left(node, parent, node_index)
        else:
            # Merge with right sibling
            self._merge_with_right(node, parent, node_index)

    def _borrow_from_left(self, node, parent, node_index):
        """Borrow from left sibling"""
        left_sibling = parent.children[node_index - 1]
        borrowed_key = left_sibling.keys.pop()
        parent_key = parent.keys[node_index - 1]

        # Put parent key in node
        node.insert_key(parent_key)
        # Put borrowed key in parent
        parent.keys[node_index - 1] = borrowed_key

        # If not leaf, transfer child too
        if not left_sibling.is_leaf:
            borrowed_child = left_sibling.children.pop()
            node.children.insert(0, borrowed_child)
            borrowed_child.parent = node

    def _borrow_from_right(self, node, parent, node_index):
        """Borrow from right sibling"""
        right_sibling = parent.children[node_index + 1]
        borrowed_key = right_sibling.keys.pop(0)
        parent_key = parent.keys[node_index]

        # Put parent key in node
        node.insert_key(parent_key)
        # Put borrowed key in parent
        parent.keys[node_index] = borrowed_key

        # If not leaf, transfer child too
        if not right_sibling.is_leaf:
            borrowed_child = right_sibling.children.pop(0)
            node.children.append(borrowed_child)
            borrowed_child.parent = node

    def _merge_with_left(self, node, parent, node_index):
        """Merge with left sibling"""
        left_sibling = parent.children[node_index - 1]
        parent_key = parent.keys.pop(node_index - 1)

        # Transfer parent key to left sibling
        left_sibling.insert_key(parent_key)
        # Transfer node keys to left sibling
        left_sibling.keys.extend(node.keys)

        # If not leaf, transfer children too
        if not node.is_leaf:
            for child in node.children:
                child.parent = left_sibling
            left_sibling.children.extend(node.children)

        # Remove node
        parent.children.pop(node_index)

        # If parent has too few keys and is not root, fix it
        if parent == self.root and not parent.keys:
            self.root = left_sibling
            left_sibling.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def _merge_with_right(self, node, parent, node_index):
        """Merge with right sibling"""
        right_sibling = parent.children[node_index + 1]
        parent_key = parent.keys.pop(node_index)

        # Transfer parent key to node
        node.insert_key(parent_key)
        # Transfer right sibling keys to node
        node.keys.extend(right_sibling.keys)

        # If not leaf, transfer children too
        if not node.is_leaf:
            for child in right_sibling.children:
                child.parent = node
            node.children.extend(right_sibling.children)

        # Remove right sibling
        parent.children.pop(node_index + 1)

        # If parent has too few keys and is not root, fix it
        if parent == self.root and not parent.keys:
            self.root = node
            node.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def _fix_node(self, node):
        """Fix a non-leaf node with too few keys"""
        if node == self.root:
            return

        parent = node.parent
        node_index = parent.children.index(node)

        # Try to borrow from left sibling
        if node_index > 0:
            left_sibling = parent.children[node_index - 1]
            if len(left_sibling.keys) > 1:
                self._borrow_from_left_nonleaf(node, parent, node_index)
                return

        # Try to borrow from right sibling
        if node_index < len(parent.children) - 1:
            right_sibling = parent.children[node_index + 1]
            if len(right_sibling.keys) > 1:
                self._borrow_from_right_nonleaf(node, parent, node_index)
                return

        # If can't borrow, merge
        if node_index > 0:
            self._merge_with_left_nonleaf(node, parent, node_index)
        else:
            self._merge_with_right_nonleaf(node, parent, node_index)

    def _borrow_from_left_nonleaf(self, node, parent, node_index):
        """Borrow from left sibling for non-leaf node"""
        left_sibling = parent.children[node_index - 1]
        parent_key = parent.keys[node_index - 1]
        borrowed_key = left_sibling.keys.pop()

        # Transfer parent key to node
        node.insert_key(parent_key)
        # Put borrowed key in parent
        parent.keys[node_index - 1] = borrowed_key

        # Transfer child
        if not left_sibling.is_leaf:
            borrowed_child = left_sibling.children.pop()
            node.children.insert(0, borrowed_child)
            borrowed_child.parent = node

    def _borrow_from_right_nonleaf(self, node, parent, node_index):
        """Borrow from right sibling for non-leaf node"""
        right_sibling = parent.children[node_index + 1]
        parent_key = parent.keys[node_index]
        borrowed_key = right_sibling.keys.pop(0)

        # Transfer parent key to node
        node.insert_key(parent_key)
        # Put borrowed key in parent
        parent.keys[node_index] = borrowed_key

        # Transfer child
        if not right_sibling.is_leaf:
            borrowed_child = right_sibling.children.pop(0)
            node.children.append(borrowed_child)
            borrowed_child.parent = node

    def _merge_with_left_nonleaf(self, node, parent, node_index):
        """Merge with left sibling for non-leaf node"""
        left_sibling = parent.children[node_index - 1]
        parent_key = parent.keys.pop(node_index - 1)

        # Transfer parent key to left sibling
        left_sibling.insert_key(parent_key)
        # Transfer node keys to left sibling
        left_sibling.keys.extend(node.keys)

        # Transfer children
        for child in node.children:
            child.parent = left_sibling
        left_sibling.children.extend(node.children)

        # Remove node
        parent.children.pop(node_index)

        # If parent has too few keys, fix it
        if parent == self.root and not parent.keys:
            self.root = left_sibling
            left_sibling.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def _merge_with_right_nonleaf(self, node, parent, node_index):
        """Merge with right sibling for non-leaf node"""
        right_sibling = parent.children[node_index + 1]
        parent_key = parent.keys.pop(node_index)

        # Transfer parent key to node
        node.insert_key(parent_key)
        # Transfer right sibling keys to node
        node.keys.extend(right_sibling.keys)

        # Transfer children
        for child in right_sibling.children:
            child.parent = node
        node.children.extend(right_sibling.children)

        # Remove right sibling
        parent.children.pop(node_index + 1)

        # If parent has too few keys, fix it
        if parent == self.root and not parent.keys:
            self.root = node
            node.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def search(self, key):
        """Search for a key"""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """Recursive search"""
        if node is None:
            return False

        if key in node.keys:
            return True

        if node.is_leaf:
            return False

        # Find appropriate child
        for i, k in enumerate(node.keys):
            if key < k:
                return self._search_recursive(node.children[i], key)
        return self._search_recursive(node.children[-1], key)

    def inorder_traversal(self, node=None, result=None):
        """Inorder traversal"""
        if result is None:
            result = []
        if node is None:
            node = self.root

        if node is None:
            return result

        if node.is_leaf:
            result.extend(node.keys)
        else:
            for i in range(len(node.keys)):
                self.inorder_traversal(node.children[i], result)
                result.append(node.keys[i])
            self.inorder_traversal(node.children[-1], result)

        return result

    def print_tree(self, node=None, level=0, child_num=0):
        """Display tree structure"""
        if node is None:
            node = self.root

        if node is None:
            print("Tree is empty")
            return

        indent = "    " * level
        prefix = f"L{level}-{child_num}: " if level > 0 else "Root: "

        # Display node keys
        keys_str = "[" + ", ".join(map(str, node.keys)) + "]"
        print(f"{indent}{prefix}{keys_str} {'(leaf)' if node.is_leaf else ''}")

        # Display children
        for i, child in enumerate(node.children):
            self.print_tree(child, level + 1, i)


if __name__ == "__main__":
    tt = TwoThreeTree()

    print("Steps to build 2-3 Tree:")
    print("=" * 60)

    # Insert values
    keys = [40, 20, 60, 10, 30, 50, 70, 25, 27, 26, 5, 15, 65, 80, 75]

    for i, key in enumerate(keys):
        tt.insert(key)
        print(f"\nAfter inserting key {key} (Step {i + 1}):")
        print(f"Inorder traversal: {tt.inorder_traversal()}")

    print("\n" + "=" * 60)
    print("Steps to delete from 2-3 Tree:")
    print("=" * 60)

    # Delete values
    delete_keys = [60, 70, 40, 25, 20]

    for i, key in enumerate(delete_keys):
        tt.delete(key)
        print(f"\nAfter deleting key {key} (Delete step {i + 1}):")
        print(f"Inorder traversal: {tt.inorder_traversal()}")

    print("\n" + "=" * 60)
    print("Final information of 2-3 Tree:")
    print("=" * 60)
    print(f"Final inorder traversal: {tt.inorder_traversal()}")

    # Search for some keys
    test_keys = [50, 75, 30, 100]
    print("\nSearch results:")
    for key in test_keys:
        found = tt.search(key)
        print(f"  Key {key}: {'Found' if found else 'Not found'}")

    print("\nFinal tree structure:")
    tt.print_tree()