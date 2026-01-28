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
        """درج کلید در گره به صورت مرتب شده"""
        self.keys.append(key)
        self.keys.sort()

    def remove_key(self, key):
        """حذف کلید از گره"""
        if key in self.keys:
            self.keys.remove(key)
            return True
        return False

    def get_child_for_key(self, key):
        """پیدا کردن فرزند مناسب برای کلید داده شده"""
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
        """درج کلید جدید"""
        print(f"\n{'=' * 50}")
        print(f"درج کلید {key}")
        print(f"{'=' * 50}")

        if self.root is None:
            self.root = Node23([key])
            print("درخت خالی بود. ایجاد ریشه جدید.")
            self.print_tree()
            return

        # پیدا کردن گره برگ برای درج
        node = self._find_leaf(self.root, key)

        # درج در گره برگ
        node.insert_key(key)

        # اگر گره بیش از حد پر شد، تقسیم آن
        if len(node.keys) == 3:
            self._split_node(node)

        print(f"بعد از درج {key}:")
        self.print_tree()

    def _find_leaf(self, node, key):
        """پیدا کردن گره برگ مناسب برای درج کلید"""
        if node.is_leaf:
            return node

        # پیدا کردن فرزند مناسب
        for i, k in enumerate(node.keys):
            if key < k:
                return self._find_leaf(node.children[i], key)
        return self._find_leaf(node.children[-1], key)

    def _split_node(self, node):
        """تقسیم گره پر"""
        if not node.is_full():
            return

        # گره وسطی برای ارتقاء به والد
        middle_key = node.keys[1]

        # ایجاد دو گره جدید
        left_node = Node23([node.keys[0]], [], node.is_leaf)
        right_node = Node23([node.keys[2]], [], node.is_leaf)

        # اگر گره برگ نباشد، فرزندان را هم تقسیم کن
        if not node.is_leaf:
            left_node.children = node.children[:2]
            right_node.children = node.children[2:]
            left_node.is_leaf = False
            right_node.is_leaf = False

            # تنظیم والد برای فرزندان
            for child in left_node.children:
                child.parent = left_node
            for child in right_node.children:
                child.parent = right_node

        # اگر گره ریشه است
        if node.parent is None:
            new_root = Node23([middle_key], [left_node, right_node], False)
            left_node.parent = new_root
            right_node.parent = new_root
            self.root = new_root
            return

        # اگر گره ریشه نیست
        parent = node.parent
        parent.insert_key(middle_key)

        # جایگزینی گره قدیمی با دو گره جدید
        index = parent.children.index(node)
        parent.children.pop(index)
        parent.children.insert(index, right_node)
        parent.children.insert(index, left_node)

        left_node.parent = parent
        right_node.parent = parent

        # اگر والد پر شد، آن را هم تقسیم کن
        if parent.is_full():
            self._split_node(parent)

    def delete(self, key):
        """حذف کلید"""
        print(f"\n{'=' * 50}")
        print(f"حذف کلید {key}")
        print(f"{'=' * 50}")

        node = self._find_node(self.root, key)
        if node is None:
            print(f"کلید {key} یافت نشد!")
            return

        if node.is_leaf:
            self._delete_from_leaf(node, key)
        else:
            # پیدا کردن جانشین (درست‌ترین گره در زیردرخت چپ)
            successor = self._find_successor(node, key)
            # جایگزینی کلید با جانشین
            key_index = node.keys.index(key)
            node.keys[key_index] = successor.keys[0]
            # حذف جانشین از برگ
            self._delete_from_leaf(successor, successor.keys[0])

        print(f"بعد از حذف {key}:")
        self.print_tree()

    def _find_node(self, node, key):
        """پیدا کردن گره حاوی کلید"""
        if node is None:
            return None

        if key in node.keys:
            return node

        if node.is_leaf:
            return None

        # پیدا کردن فرزند مناسب
        for i, k in enumerate(node.keys):
            if key < k:
                return self._find_node(node.children[i], key)
        return self._find_node(node.children[-1], key)

    def _find_successor(self, node, key):
        """پیدا کردن جانشین برای کلید"""
        key_index = node.keys.index(key)
        current = node.children[key_index + 1]
        while not current.is_leaf:
            current = current.children[0]
        return current

    def _delete_from_leaf(self, node, key):
        """حذف کلید از گره برگ"""
        if not node.remove_key(key):
            return

        # اگر گره ریشه است و خالی شده
        if node == self.root and not node.keys:
            self.root = None
            return

        # اگر گره برگ خیلی کم کلید دارد، اصلاح کن
        if len(node.keys) < 1 and node != self.root:
            self._fix_leaf(node)

    def _fix_leaf(self, node):
        """اصلاح گره برگ که کم کلید دارد"""
        parent = node.parent
        node_index = parent.children.index(node)

        # سعی کن از برادر چپ قرض بگیری
        if node_index > 0:
            left_sibling = parent.children[node_index - 1]
            if len(left_sibling.keys) > 1:
                self._borrow_from_left(node, parent, node_index)
                return

        # سعی کن از برادر راست قرض بگیری
        if node_index < len(parent.children) - 1:
            right_sibling = parent.children[node_index + 1]
            if len(right_sibling.keys) > 1:
                self._borrow_from_right(node, parent, node_index)
                return

        # اگر نتوانستیم قرض بگیریم، ادغام کن
        if node_index > 0:
            # ادغام با برادر چپ
            self._merge_with_left(node, parent, node_index)
        else:
            # ادغام با برادر راست
            self._merge_with_right(node, parent, node_index)

    def _borrow_from_left(self, node, parent, node_index):
        """قرض گرفتن از برادر چپ"""
        left_sibling = parent.children[node_index - 1]
        borrowed_key = left_sibling.keys.pop()
        parent_key = parent.keys[node_index - 1]

        # قرار دادن کلید والد در گره
        node.insert_key(parent_key)
        # قرار دادن کلید قرض گرفته شده در والد
        parent.keys[node_index - 1] = borrowed_key

        # اگر گره برگ نیست، فرزند هم انتقال بده
        if not left_sibling.is_leaf:
            borrowed_child = left_sibling.children.pop()
            node.children.insert(0, borrowed_child)
            borrowed_child.parent = node

    def _borrow_from_right(self, node, parent, node_index):
        """قرض گرفتن از برادر راست"""
        right_sibling = parent.children[node_index + 1]
        borrowed_key = right_sibling.keys.pop(0)
        parent_key = parent.keys[node_index]

        # قرار دادن کلید والد در گره
        node.insert_key(parent_key)
        # قرار دادن کلید قرض گرفته شده در والد
        parent.keys[node_index] = borrowed_key

        # اگر گره برگ نیست، فرزند هم انتقال بده
        if not right_sibling.is_leaf:
            borrowed_child = right_sibling.children.pop(0)
            node.children.append(borrowed_child)
            borrowed_child.parent = node

    def _merge_with_left(self, node, parent, node_index):
        """ادغام با برادر چپ"""
        left_sibling = parent.children[node_index - 1]
        parent_key = parent.keys.pop(node_index - 1)

        # انتقال کلید والد به برادر چپ
        left_sibling.insert_key(parent_key)
        # انتقال کلیدهای گره به برادر چپ
        left_sibling.keys.extend(node.keys)

        # اگر گره برگ نیست، فرزندان را هم انتقال بده
        if not node.is_leaf:
            for child in node.children:
                child.parent = left_sibling
            left_sibling.children.extend(node.children)

        # حذف گره
        parent.children.pop(node_index)

        # اگر والد کم کلید دارد و ریشه نیست، اصلاح کن
        if parent == self.root and not parent.keys:
            self.root = left_sibling
            left_sibling.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def _merge_with_right(self, node, parent, node_index):
        """ادغام با برادر راست"""
        right_sibling = parent.children[node_index + 1]
        parent_key = parent.keys.pop(node_index)

        # انتقال کلید والد به گره
        node.insert_key(parent_key)
        # انتقال کلیدهای برادر راست به گره
        node.keys.extend(right_sibling.keys)

        # اگر گره برگ نیست، فرزندان را هم انتقال بده
        if not node.is_leaf:
            for child in right_sibling.children:
                child.parent = node
            node.children.extend(right_sibling.children)

        # حذف برادر راست
        parent.children.pop(node_index + 1)

        # اگر والد کم کلید دارد و ریشه نیست، اصلاح کن
        if parent == self.root and not parent.keys:
            self.root = node
            node.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def _fix_node(self, node):
        """اصلاح گره غیربرگ که کم کلید دارد"""
        if node == self.root:
            return

        parent = node.parent
        node_index = parent.children.index(node)

        # سعی کن از برادر چپ قرض بگیری
        if node_index > 0:
            left_sibling = parent.children[node_index - 1]
            if len(left_sibling.keys) > 1:
                self._borrow_from_left_nonleaf(node, parent, node_index)
                return

        # سعی کن از برادر راست قرض بگیری
        if node_index < len(parent.children) - 1:
            right_sibling = parent.children[node_index + 1]
            if len(right_sibling.keys) > 1:
                self._borrow_from_right_nonleaf(node, parent, node_index)
                return

        # اگر نتوانستیم قرض بگیریم، ادغام کن
        if node_index > 0:
            self._merge_with_left_nonleaf(node, parent, node_index)
        else:
            self._merge_with_right_nonleaf(node, parent, node_index)

    def _borrow_from_left_nonleaf(self, node, parent, node_index):
        """قرض گرفتن از برادر چپ برای گره غیربرگ"""
        left_sibling = parent.children[node_index - 1]
        parent_key = parent.keys[node_index - 1]
        borrowed_key = left_sibling.keys.pop()

        # انتقال کلید والد به گره
        node.insert_key(parent_key)
        # قرار دادن کلید قرض گرفته شده در والد
        parent.keys[node_index - 1] = borrowed_key

        # انتقال فرزند
        if not left_sibling.is_leaf:
            borrowed_child = left_sibling.children.pop()
            node.children.insert(0, borrowed_child)
            borrowed_child.parent = node

    def _borrow_from_right_nonleaf(self, node, parent, node_index):
        """قرض گرفتن از برادر راست برای گره غیربرگ"""
        right_sibling = parent.children[node_index + 1]
        parent_key = parent.keys[node_index]
        borrowed_key = right_sibling.keys.pop(0)

        # انتقال کلید والد به گره
        node.insert_key(parent_key)
        # قرار دادن کلید قرض گرفته شده در والد
        parent.keys[node_index] = borrowed_key

        # انتقال فرزند
        if not right_sibling.is_leaf:
            borrowed_child = right_sibling.children.pop(0)
            node.children.append(borrowed_child)
            borrowed_child.parent = node

    def _merge_with_left_nonleaf(self, node, parent, node_index):
        """ادغام با برادر چپ برای گره غیربرگ"""
        left_sibling = parent.children[node_index - 1]
        parent_key = parent.keys.pop(node_index - 1)

        # انتقال کلید والد به برادر چپ
        left_sibling.insert_key(parent_key)
        # انتقال کلیدهای گره به برادر چپ
        left_sibling.keys.extend(node.keys)

        # انتقال فرزندان
        for child in node.children:
            child.parent = left_sibling
        left_sibling.children.extend(node.children)

        # حذف گره
        parent.children.pop(node_index)

        # اگر والد کم کلید دارد، اصلاح کن
        if parent == self.root and not parent.keys:
            self.root = left_sibling
            left_sibling.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def _merge_with_right_nonleaf(self, node, parent, node_index):
        """ادغام با برادر راست برای گره غیربرگ"""
        right_sibling = parent.children[node_index + 1]
        parent_key = parent.keys.pop(node_index)

        # انتقال کلید والد به گره
        node.insert_key(parent_key)
        # انتقال کلیدهای برادر راست به گره
        node.keys.extend(right_sibling.keys)

        # انتقال فرزندان
        for child in right_sibling.children:
            child.parent = node
        node.children.extend(right_sibling.children)

        # حذف برادر راست
        parent.children.pop(node_index + 1)

        # اگر والد کم کلید دارد، اصلاح کن
        if parent == self.root and not parent.keys:
            self.root = node
            node.parent = None
        elif parent != self.root and len(parent.keys) < 1:
            self._fix_node(parent)

    def search(self, key):
        """جستجوی کلید"""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """جستجوی بازگشتی"""
        if node is None:
            return False

        if key in node.keys:
            return True

        if node.is_leaf:
            return False

        # پیدا کردن فرزند مناسب
        for i, k in enumerate(node.keys):
            if key < k:
                return self._search_recursive(node.children[i], key)
        return self._search_recursive(node.children[-1], key)

    def inorder_traversal(self, node=None, result=None):
        """پیمایش میان‌ترتیبی"""
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
        """نمایش درخت"""
        if node is None:
            node = self.root

        if node is None:
            print("درخت خالی است")
            return

        indent = "    " * level
        prefix = f"L{level}-{child_num}: " if level > 0 else "Root: "

        # نمایش کلیدهای گره
        keys_str = "[" + ", ".join(map(str, node.keys)) + "]"
        print(f"{indent}{prefix}{keys_str} {'(leaf)' if node.is_leaf else ''}")

        # نمایش فرزندان
        for i, child in enumerate(node.children):
            self.print_tree(child, level + 1, i)


if __name__ == "__main__":
    tt = TwoThreeTree()

    print("مراحل ساخت درخت 2-3:")
    print("=" * 60)

    # درج مقادیر
    keys = [40, 20, 60, 10, 30, 50, 70, 25, 27, 26, 5, 15, 65, 80, 75]

    for i, key in enumerate(keys):
        tt.insert(key)
        print(f"\nپس از درج کلید {key} (گام {i + 1}):")
        print(f"پیمایش inorder: {tt.inorder_traversal()}")

    print("\n" + "=" * 60)
    print("مراحل حذف از درخت 2-3:")
    print("=" * 60)

    # حذف مقادیر
    delete_keys = [60, 70, 40, 25, 20]

    for i, key in enumerate(delete_keys):
        tt.delete(key)
        print(f"\nپس از حذف کلید {key} (گام حذف {i + 1}):")
        print(f"پیمایش inorder: {tt.inorder_traversal()}")

    print("\n" + "=" * 60)
    print("اطلاعات نهایی درخت 2-3:")
    print("=" * 60)
    print(f"پیمایش inorder نهایی: {tt.inorder_traversal()}")

    # جستجوی برخی کلیدها
    test_keys = [50, 75, 30, 100]
    print("\nنتایج جستجو:")
    for key in test_keys:
        found = tt.search(key)
        print(f"  کلید {key}: {'یافت شد' if found else 'یافت نشد'}")

    print("\nساختار نهایی درخت:")
    tt.print_tree()