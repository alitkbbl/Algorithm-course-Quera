import random
from typing import Any, Optional


class Node:
    """Node class for storing data in Skip List"""

    def __init__(self, key: Any, value: Any = None, level: int = 0):
        """
        Node constructor

        Parameters:
        key: Node key (for comparison and ordering)
        value: Stored value (optional)
        level: Node level in Skip List
        """
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)  # List of pointers to next nodes at each level

    def __repr__(self):
        return f"Node(key={self.key}, value={self.value}, level={len(self.forward) - 1})"


class SkipList:
    """Skip List class"""

    def __init__(self, max_level: int = 4, p: float = 0.5):
        """
        Skip List constructor

        Parameters:
        max_level: Maximum allowed level for nodes
        p: Probability of increasing level for a node (typically 0.5)
        """
        self.max_level = max_level
        self.p = p  # Probability for level increase
        self.level = 0  # Current level of Skip List
        self.header = Node(None, None, max_level)  # Header node (starting point)
        self.size = 0  # Number of elements in Skip List

    def random_level(self) -> int:
        """
        Generate random level for a new node

        Returns:
        Random level based on probability p
        """
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a key in Skip List

        Parameters:
        key: Key to search for

        Returns:
        Value associated with the key, or None if not found
        """
        current = self.header

        # Start from the highest level and move down
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        # Move to the next node at level 0
        current = current.forward[0]

        # If found, return the value
        if current and current.key == key:
            return current.value
        return None

    def insert(self, key: Any, value: Any = None) -> None:
        """
        Insert a new key-value pair into Skip List

        Parameters:
        key: Key to insert
        value: Value to associate with the key
        """
        # Array to store update pointers
        update = [None] * (self.max_level + 1)
        current = self.header

        # Find the position to insert and track update nodes
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Move to the next node at level 0
        current = current.forward[0]

        # If key already exists, update the value
        if current and current.key == key:
            current.value = value
            return

        # Generate random level for new node
        new_level = self.random_level()

        # If new level is higher than current level, update header
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level

        # Create new node
        new_node = Node(key, value, new_level)

        # Update forward pointers
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

        self.size += 1

    def delete(self, key: Any) -> bool:
        """
        Delete a key from Skip List

        Parameters:
        key: Key to delete

        Returns:
        True if key was found and deleted, False otherwise
        """
        # Array to store update pointers
        update = [None] * (self.max_level + 1)
        current = self.header

        # Find the node to delete and track update nodes
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Move to the next node at level 0
        current = current.forward[0]

        # If key not found, return False
        if not current or current.key != key:
            return False

        # Update forward pointers to bypass the deleted node
        for i in range(self.level + 1):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]

        # Update skip list level if needed
        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1

        self.size -= 1
        return True

    def display(self) -> None:
        """Display all levels of Skip List"""
        print("\nSkip List Structure:")
        print(f"Level: {self.level}, Size: {self.size}")

        for i in range(self.level, -1, -1):
            current = self.header.forward[i]
            print(f"Level {i}: ", end="")

            while current:
                print(f"[{current.key}:{current.value}] -> ", end="")
                current = current.forward[i]
            print("None")

    def traverse(self) -> list:
        """
        Traverse Skip List in sorted order

        Returns:
        List of (key, value) pairs in sorted order
        """
        result = []
        current = self.header.forward[0]

        while current:
            result.append((current.key, current.value))
            current = current.forward[0]

        return result

    def find_range(self, start_key: Any, end_key: Any) -> list:
        """
        Find all keys in a range

        Parameters:
        start_key: Starting key (inclusive)
        end_key: Ending key (inclusive)

        Returns:
        List of (key, value) pairs within the range
        """
        result = []
        current = self.header

        # Find the starting position
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < start_key:
                current = current.forward[i]

        current = current.forward[0]

        # Collect all keys in range
        while current and current.key <= end_key:
            result.append((current.key, current.value))
            current = current.forward[0]

        return result


# Example Usage and Test Cases
def main():
    """Example usage of Skip List"""

    print("=== Skip List Implementation Examples ===")

    # Create a skip list
    print("\n1. Creating Skip List with max_level=4")
    skip_list = SkipList(max_level=4, p=0.5)

    # Insert elements
    print("\n2. Inserting key-value pairs:")
    test_data = [
        (3, "Apple"),
        (7, "Banana"),
        (2, "Cherry"),
        (5, "Date"),
        (1, "Elderberry"),
        (9, "Fig"),
        (4, "Grape"),
        (8, "Honeydew"),
        (6, "Kiwi")
    ]

    for key, value in test_data:
        skip_list.insert(key, value)
        print(f"   Inserted: {key} -> {value}")

    # Display structure
    skip_list.display()

    # Search examples
    print("\n3. Search Examples:")
    search_keys = [5, 2, 10, 1]
    for key in search_keys:
        result = skip_list.search(key)
        if result:
            print(f"   Key {key} found: {result}")
        else:
            print(f"   Key {key} not found")

    # Traverse all elements
    print("\n4. All elements in sorted order:")
    elements = skip_list.traverse()
    for key, value in elements:
        print(f"   {key}: {value}")

    # Range query
    print("\n5. Range query (keys 3 to 7):")
    range_result = skip_list.find_range(3, 7)
    for key, value in range_result:
        print(f"   {key}: {value}")

    # Delete examples
    print("\n6. Delete Examples:")
    delete_keys = [5, 10, 2]
    for key in delete_keys:
        if skip_list.delete(key):
            print(f"   Key {key} deleted successfully")
        else:
            print(f"   Key {key} not found for deletion")

    # Display after deletion
    print("\n7. Skip List after deletions:")
    skip_list.display()

    # Insert more elements
    print("\n8. Inserting more elements:")

    skip_list.insert(10, "Jackfruit")
    skip_list.insert(0, "Lemon")
    skip_list.insert(11, "Mango")

    skip_list.display()

    # Performance comparison
    print("\n9. Performance Test:")
    print("   Inserting 1000 random elements...")
    big_skip_list = SkipList(max_level=6)

    import time
    start_time = time.time()

    for i in range(1000):
        key = random.randint(1, 10000)
        big_skip_list.insert(key, f"Value_{key}")

    insert_time = time.time() - start_time
    print(f"   Time taken for 1000 inserts: {insert_time:.4f} seconds")

    # Search performance
    start_time = time.time()
    for i in range(100):
        key = random.randint(1, 10000)
        big_skip_list.search(key)

    search_time = time.time() - start_time
    print(f"   Time for 100 searches: {search_time:.4f} seconds")


if __name__ == "__main__":
    main()

# Key Concepts Explained:

# 1. Skip List Structure:
#    - Multi-level linked list where higher levels skip more elements
#    - Level 0 contains all elements in sorted order
#    - Higher levels contain subsets of elements with "express lanes"

# 2. Time Complexity (Average Case):
#    - Search: O(log n)
#    - Insert: O(log n)
#    - Delete: O(log n)
#    - Space: O(n) average, O(n log n) worst case

# 3. Advantages over Balanced Trees:
#    - Simpler to implement
#    - Probabilistic balancing (no complex rotations)
#    - Good cache performance
#    - Easy to implement concurrent operations

# 4. Common Use Cases:
#    - Database indexing
#    - Priority queues
#    - Range queries
#    - Implementing ordered maps/sets

# 5. Probability Parameter (p):
#    - Typically set to 0.5
#    - Higher p = more nodes in higher levels = faster search but more memory
#    - Lower p = fewer nodes in higher levels = slower search but less memory