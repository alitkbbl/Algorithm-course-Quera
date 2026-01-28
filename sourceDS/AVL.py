class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        # 1. Normal BST insertion
        if not root:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed

        # 2. Update height of the parent node
        self.update_height(root)

        # 3. Check balance and perform necessary rotations
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert_key(self, key):
        print(f"\n{'=' * 50}")
        print(f"Inserting key {key}")
        print(f"{'=' * 50}")
        self.root = self.insert(self.root, key)

    def delete(self, root, key):
        # 1. Normal BST deletion
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: find the smallest node in the right subtree
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        # 2. Update height
        self.update_height(root)

        # 3. Check balance and perform necessary rotations
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete_key(self, key):
        print(f"\n{'=' * 50}")
        print(f"Deleting key {key}")
        print(f"{'=' * 50}")
        self.root = self.delete(self.root, key)

    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def search_key(self, key):
        return self.search(self.root, key) is not None

    def inorder_traversal(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.key)
            self.inorder_traversal(root.right, result)
        return result

    def preorder_traversal(self, root, result=None):
        if result is None:
            result = []
        if root:
            result.append(root.key)
            self.preorder_traversal(root.left, result)
            self.preorder_traversal(root.right, result)
        return result

    def level_order_traversal(self):
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.key)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result

    def print_tree_visual(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if node is not None:
            if node.right:
                self.print_tree_visual(node.right, prefix + ("│   " if is_left else "    "), False)
            print(
                prefix + ("└── " if is_left else "┌── ") + f"{node.key} (h={node.height}, b={self.get_balance(node)})")
            if node.left:
                self.print_tree_visual(node.left, prefix + ("    " if is_left else "│   "), True)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        if node:
            print(" " * (level * 4) + prefix + str(node.key) + f" (h={node.height}, b={self.get_balance(node)})")
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
        elif level == 0:
            print("Tree is empty")


# Test AVL Tree
if __name__ == "__main__":
    avl = AVLTree()

    print("Steps to build AVL Tree:")
    print("=" * 60)

    # Insert values
    keys = [40, 20, 60, 10, 30, 50, 70, 25, 27, 26, 5, 15, 65, 80, 75]

    for i, key in enumerate(keys):
        avl.insert_key(key)
        print(f"\nAfter inserting key {key} (Step {i + 1}):")
        print("-" * 40)
        avl.print_tree_visual()
        print(f"\nInorder traversal: {avl.inorder_traversal(avl.root)}")

    print("\n" + "=" * 60)
    print("Steps to delete from AVL Tree:")
    print("=" * 60)

    # Delete values
    delete_keys = [60, 70, 40, 25, 20]

    for i, key in enumerate(delete_keys):
        avl.delete_key(key)
        print(f"\nAfter deleting key {key} (Delete step {i + 1}):")
        print("-" * 40)
        avl.print_tree_visual()
        print(f"\nInorder traversal: {avl.inorder_traversal(avl.root)}")

    print("\n" + "=" * 60)
    print("Final tree information:")
    print("=" * 60)
    print(f"Final root: {avl.root.key if avl.root else 'None'}")
    print(f"Tree height: {avl.get_height(avl.root)}")
    print(f"Final inorder traversal: {avl.inorder_traversal(avl.root)}")
    print(f"Final level-order traversal: {avl.level_order_traversal()}")
    print("\nFinal graphical display:")
    avl.print_tree_visual()