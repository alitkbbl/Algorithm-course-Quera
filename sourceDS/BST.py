class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        # If tree is empty, create new node as root
        if root is None:
            print(f"  Inserted {key} as new node")
            return TreeNode(key)

        # Otherwise, recur down the tree
        if key < root.key:
            print(f"  {key} < {root.key}, going left")
            root.left = self.insert(root.left, key)
        elif key > root.key:
            print(f"  {key} > {root.key}, going right")
            root.right = self.insert(root.right, key)
        else:
            print(f"  Key {key} already exists (duplicate not inserted)")

        return root

    def insert_key(self, key):
        print(f"\n{'=' * 50}")
        print(f"INSERTING KEY {key}")
        print(f"{'=' * 50}")

        if self.root is None:
            print(f"Tree is empty. Creating root with key {key}")
            self.root = TreeNode(key)
        else:
            print(f"Starting from root: {self.root.key}")
            self.root = self.insert(self.root, key)

        self.print_tree()

    def delete(self, root, key):
        # Base case: empty tree
        if root is None:
            print(f"  Key {key} not found in tree")
            return root

        print(f"  Current node: {root.key}")

        # Recur down the tree
        if key < root.key:
            print(f"  {key} < {root.key}, searching left subtree")
            root.left = self.delete(root.left, key)
        elif key > root.key:
            print(f"  {key} > {root.key}, searching right subtree")
            root.right = self.delete(root.right, key)
        else:
            # Node to delete found
            print(f"  Found node to delete: {root.key}")

            # Node with only one child or no child
            if root.left is None:
                print(f"  Node has no left child, returning right child: {root.right.key if root.right else 'None'}")
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                print(f"  Node has no right child, returning left child: {root.left.key}")
                temp = root.left
                root = None
                return temp

            # Node with two children: get inorder successor (smallest in right subtree)
            print(f"  Node has two children, finding inorder successor")
            temp = self.min_value_node(root.right)
            print(f"  Inorder successor found: {temp.key}")
            print(f"  Copying {temp.key} to current node {root.key}")
            root.key = temp.key

            # Delete the inorder successor
            print(f"  Deleting inorder successor {temp.key} from right subtree")
            root.right = self.delete(root.right, temp.key)

        return root

    def delete_key(self, key):
        print(f"\n{'=' * 50}")
        print(f"DELETING KEY {key}")
        print(f"{'=' * 50}")

        if self.root is None:
            print("Tree is empty, nothing to delete")
            return

        print(f"Starting search from root: {self.root.key}")
        self.root = self.delete(self.root, key)

        if self.root:
            print(f"\nAfter deletion of {key}:")
            self.print_tree()
        else:
            print("Tree is now empty")

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, root, key):
        # Base cases: root is null or key is present at root
        if root is None or root.key == key:
            return root

        # Key is greater than root's key
        if key > root.key:
            return self.search(root.right, key)

        # Key is smaller than root's key
        return self.search(root.left, key)

    def search_key(self, key):
        print(f"\n{'=' * 50}")
        print(f"SEARCHING FOR KEY {key}")
        print(f"{'=' * 50}")

        result = self.search(self.root, key)

        if result:
            print(f"✓ Key {key} FOUND in the tree")
        else:
            print(f"✗ Key {key} NOT FOUND in the tree")

        return result is not None

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

    def postorder_traversal(self, root, result=None):
        if result is None:
            result = []

        if root:
            self.postorder_traversal(root.left, result)
            self.postorder_traversal(root.right, result)
            result.append(root.key)

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

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return max(left_height, right_height) + 1

    def print_tree_visual(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root

        if node is not None:
            if node.right:
                self.print_tree_visual(node.right, prefix + ("│   " if is_left else "    "), False)

            print(prefix + ("└── " if is_left else "┌── ") + str(node.key))

            if node.left:
                self.print_tree_visual(node.left, prefix + ("    " if is_left else "│   "), True)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        if node:
            print(" " * (level * 4) + prefix + str(node.key))

            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
        elif level == 0:
            print("Tree is empty")


# Test Binary Search Tree
if __name__ == "__main__":
    bst = BinarySearchTree()

    print("BINARY SEARCH TREE DEMONSTRATION")
    print("=" * 60)

    # Insert values
    print("\nPHASE 1: INSERTING KEYS")
    print("-" * 60)

    keys = [40, 20, 60, 10, 30, 50, 70, 25, 27, 26, 5, 15, 65, 80, 75]

    for i, key in enumerate(keys):
        bst.insert_key(key)
        print(f"\nStep {i + 1} Summary:")
        print(f"Inorder traversal: {bst.inorder_traversal(bst.root)}")
        print(f"Tree height: {bst.height(bst.root)}")
        print("-" * 40)

    # Search for some keys
    print("\nPHASE 2: SEARCHING KEYS")
    print("-" * 60)

    search_keys = [40, 25, 100, 75, 5]

    for key in search_keys:
        bst.search_key(key)

    # Traversal demonstrations
    print("\nPHASE 3: TREE TRAVERSALS")
    print("-" * 60)

    print(f"Inorder traversal (sorted): {bst.inorder_traversal(bst.root)}")
    print(f"Preorder traversal: {bst.preorder_traversal(bst.root)}")
    print(f"Postorder traversal: {bst.postorder_traversal(bst.root)}")
    print(f"Level-order traversal: {bst.level_order_traversal()}")

    # Delete values
    print("\nPHASE 4: DELETING KEYS")
    print("-" * 60)

    delete_keys = [60, 70, 40, 25, 20]

    for i, key in enumerate(delete_keys):
        bst.delete_key(key)
        print(f"\nAfter deletion {i + 1}:")
        print(f"Inorder traversal: {bst.inorder_traversal(bst.root)}")
        print(f"Tree height: {bst.height(bst.root)}")
        print("-" * 40)

    # Final tree information
    print("\nFINAL TREE INFORMATION")
    print("=" * 60)

    print(f"Root: {bst.root.key if bst.root else 'None'}")
    print(f"Tree height: {bst.height(bst.root)}")
    print(f"Final inorder traversal: {bst.inorder_traversal(bst.root)}")
    print(f"Final preorder traversal: {bst.preorder_traversal(bst.root)}")
    print(f"Final level-order traversal: {bst.level_order_traversal()}")

    print("\nFINAL TREE STRUCTURE (Graphical):")
    print("-" * 40)
    bst.print_tree_visual()

    print("\nFINAL TREE STRUCTURE (Hierarchical):")
    print("-" * 40)
    bst.print_tree()