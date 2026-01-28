RED = True
BLACK = False


class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = RED  # New node is always red
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(0)  # NIL node (leaf)
        self.NIL.color = BLACK
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def left_rotate(self, x):
        """Left rotation"""
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        """Right rotation"""
        x = y.left
        y.left = x.right

        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent

        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def insert(self, key):
        """Insert new key"""
        print(f"\n{'=' * 50}")
        print(f"Inserting key {key}")
        print(f"{'=' * 50}")

        node = RBNode(key)
        node.parent = self.NIL
        node.left = self.NIL
        node.right = self.NIL
        node.color = RED  # New node is always red

        y = self.NIL
        x = self.root

        # Find appropriate location for insertion
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if y == self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # If node is root
        if node.parent == self.NIL:
            node.color = BLACK
            return

        # If grandparent is NIL
        if node.parent.parent == self.NIL:
            return

        # Fix tree to maintain Red-Black properties
        self._fix_insert(node)

        # Display tree after insertion
        print(f"After inserting {key}:")
        self.print_tree()

    def _fix_insert(self, k):
        """Fix tree after insertion"""
        while k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u.color == RED:
                    # Case 1: Uncle is red
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Case 2: Uncle is black and node is left child
                        k = k.parent
                        self.right_rotate(k)
                    # Case 3: Uncle is black and node is right child
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle

                if u.color == RED:
                    # Case 1: Uncle is red
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Case 2: Uncle is black and node is right child
                        k = k.parent
                        self.left_rotate(k)
                    # Case 3: Uncle is black and node is left child
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = BLACK

    def delete(self, key):
        """Delete a key"""
        print(f"\n{'=' * 50}")
        print(f"Deleting key {key}")
        print(f"{'=' * 50}")

        # Find node to delete
        z = self._search(self.root, key)
        if z == self.NIL:
            print(f"Key {key} not found!")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == BLACK:
            self._fix_delete(x)

        # Display tree after deletion
        print(f"After deleting {key}:")
        self.print_tree()

    def _fix_delete(self, x):
        """Fix tree after deletion"""
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == RED:
                    # Case 1: Sibling is red
                    s.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == BLACK and s.right.color == BLACK:
                    # Case 2: Both sibling's children are black
                    s.color = RED
                    x = x.parent
                else:
                    if s.right.color == BLACK:
                        # Case 3: Sibling's right child is black
                        s.left.color = BLACK
                        s.color = RED
                        self.right_rotate(s)
                        s = x.parent.right

                    # Case 4: Sibling's right child is red
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == RED:
                    # Case 1: Sibling is red
                    s.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == BLACK and s.left.color == BLACK:
                    # Case 2: Both sibling's children are black
                    s.color = RED
                    x = x.parent
                else:
                    if s.left.color == BLACK:
                        # Case 3: Sibling's left child is black
                        s.right.color = BLACK
                        s.color = RED
                        self.left_rotate(s)
                        s = x.parent.left

                    # Case 4: Sibling's left child is red
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = BLACK

    def _rb_transplant(self, u, v):
        """Replace subtree u with subtree v"""
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        """Find minimum node in subtree"""
        while node.left != self.NIL:
            node = node.left
        return node

    def _search(self, node, key):
        """Search for node with given key"""
        if node == self.NIL or key == node.key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        """Public search method"""
        return self._search(self.root, key) != self.NIL

    def inorder_traversal(self, node=None, result=None):
        """Inorder traversal"""
        if result is None:
            result = []
        if node is None:
            node = self.root

        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append((node.key, 'R' if node.color == RED else 'B'))
            self.inorder_traversal(node.right, result)

        return result

    def level_order_traversal(self):
        """Level-order traversal"""
        if self.root == self.NIL:
            return []

        result = []
        queue = [(self.root, 0)]

        while queue:
            node, level = queue.pop(0)
            if len(result) <= level:
                result.append([])

            result[level].append((node.key, 'R' if node.color == RED else 'B'))

            if node.left != self.NIL:
                queue.append((node.left, level + 1))
            if node.right != self.NIL:
                queue.append((node.right, level + 1))

        return result

    def print_tree(self, node=None, indent="", last=True):
        """Graphical display of tree"""
        if node is None:
            node = self.root

        if node == self.NIL:
            return

        prefix = "└── " if last else "├── "
        color = "🔴" if node.color == RED else "⚫"

        if node == self.root:
            print(f"Root: {node.key}{color}")
        else:
            print(indent + prefix + f"{node.key}{color}")

        indent += "    " if last else "│   "

        # Display children
        children = []
        if node.left != self.NIL:
            children.append(node.left)
        if node.right != self.NIL:
            children.append(node.right)

        for i, child in enumerate(children):
            self.print_tree(child, indent, i == len(children) - 1)


# Test Red-Black Tree
if __name__ == "__main__":
    rbt = RedBlackTree()

    print("Steps to build Red-Black Tree:")
    print("=" * 60)

    # Insert values
    keys = [40, 20, 60, 10, 30, 50, 70, 25, 27, 26, 5, 15, 65, 80, 75]

    for i, key in enumerate(keys):
        rbt.insert(key)
        print(f"\nAfter inserting key {key} (Step {i + 1}):")
        print(f"Inorder traversal: {rbt.inorder_traversal()}")

    print("\n" + "=" * 60)
    print("Steps to delete from Red-Black Tree:")
    print("=" * 60)

    # Delete values
    delete_keys = [60, 70, 40, 25, 20]

    for i, key in enumerate(delete_keys):
        rbt.delete(key)
        print(f"\nAfter deleting key {key} (Delete step {i + 1}):")
        print(f"Inorder traversal: {rbt.inorder_traversal()}")

    print("\n" + "=" * 60)
    print("Final information of Red-Black Tree:")
    print("=" * 60)
    print(f"Final root: {rbt.root.key if rbt.root != rbt.NIL else 'None'}")
    print(f"Final inorder traversal: {rbt.inorder_traversal()}")
    print(f"Final level-order traversal:")

    level_order = rbt.level_order_traversal()
    for level in level_order:
        print(f"  Level {level_order.index(level)}: {level}")

    print("\nFinal graphical display:")
    rbt.print_tree()