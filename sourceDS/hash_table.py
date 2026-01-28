class HashTable:
    def __init__(self, size=10):
        """
        Initialize hash table with given size
        Each slot initially contains None
        """
        self.size = size
        self.table = [None] * size  # Main storage array
        self.count = 0  # Number of elements stored

    def _hash_function(self, key):
        """
        Hash function: converts key to index
        """
        if isinstance(key, str):
            # For strings: sum of ASCII codes
            hash_sum = 0
            for char in key:
                hash_sum += ord(char)  # Get ASCII value
            return hash_sum % self.size
        else:
            # For numbers and other types
            return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into hash table
        Uses Linear Probing to handle collisions
        """
        # If table is too full, resize it
        if self.count >= self.size * 0.7:  # Load factor threshold
            self._resize_table()

        # Calculate initial index
        index = self._hash_function(key)
        start_index = index

        # Linear probing: find empty slot
        while self.table[index] is not None:
            # Check if key already exists
            if self.table[index][0] == key:  # [0] is key, [1] is value
                # Update existing key's value
                self.table[index] = (key, value)
                return

            # Move to next slot (linear probing)
            index = (index + 1) % self.size

            # Check if we've searched all slots
            if index == start_index:
                # This should not happen due to resizing
                raise Exception("Hash table is full")

        # Found empty slot, insert key-value pair
        self.table[index] = (key, value)
        self.count += 1

    def search(self, key):
        """
        Search for a key and return its value
        Returns None if key not found
        """
        index = self._hash_function(key)
        start_index = index

        # Linear probing search
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Return value

            # Move to next slot
            index = (index + 1) % self.size

            # If we've checked all slots
            if index == start_index:
                break

        return None  # Key not found

    def delete(self, key):
        """
        Delete a key-value pair from hash table
        Returns True if deleted, False if not found
        """
        index = self._hash_function(key)
        start_index = index

        # Search for the key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                # Mark as deleted (special marker)
                self.table[index] = "DELETED"
                self.count -= 1
                return True

            # Move to next slot
            index = (index + 1) % self.size

            # Check if we've searched all slots
            if index == start_index:
                break

        return False  # Key not found

    def _resize_table(self):
        """
        Resize table when it becomes too full
        Double the size and rehash all elements
        """
        old_table = self.table
        old_size = self.size

        # Double the size
        self.size = self.size * 2
        self.table = [None] * self.size
        self.count = 0  # Reset count

        print(f"Resizing table from {old_size} to {self.size}")

        # Rehash all elements from old table
        for item in old_table:
            if item is not None and item != "DELETED":
                self.insert(item[0], item[1])

    def display(self):
        """
        Display hash table contents
        Shows index, key, and value for each slot
        """
        print(f"\n{'=' * 50}")
        print(f"HASH TABLE - Size: {self.size}, Elements: {self.count}")
        print(f"{'=' * 50}")
        print(f"{'Index':<8} {'Key':<15} {'Value':<15} {'Status':<10}")
        print(f"{'-' * 50}")

        for i in range(self.size):
            item = self.table[i]
            if item is None:
                print(f"{i:<8} {'-':<15} {'-':<15} EMPTY")
            elif item == "DELETED":
                print(f"{i:<8} {'-':<15} {'-':<15} DELETED")
            else:
                print(f"{i:<8} {str(item[0]):<15} {str(item[1]):<15} OCCUPIED")

        print(f"{'=' * 50}")

    def get_load_factor(self):
        """
        Calculate and return current load factor
        """
        return self.count / self.size if self.size > 0 else 0


# Advanced Version with Better Performance
class AdvancedHashTable:
    def __init__(self, size=10):
        """
        Advanced hash table with separate arrays for better memory management
        """
        self.size = size
        self.keys = [None] * size  # Array for keys
        self.values = [None] * size  # Array for values
        self.flags = [0] * size  # 0=empty, 1=occupied, 2=deleted
        self.count = 0

    def _hash_function(self, key):
        """
        Better hash function with prime number multiplication
        """
        if isinstance(key, str):
            hash_val = 0
            prime = 31  # Common prime for hash functions
            for char in key:
                hash_val = (hash_val * prime + ord(char)) % self.size
            return hash_val
        else:
            return (key * 2654435761) % self.size  # Multiplication by golden ratio constant

    def insert(self, key, value):
        """
        Insert with lazy deletion support
        """
        # Check load factor and resize if needed
        if self.count >= self.size * 0.75:
            self._resize()

        index = self._hash_function(key)

        # Linear probing
        while self.flags[index] == 1:  # While slot is occupied
            if self.keys[index] == key:  # Key exists, update value
                self.values[index] = value
                return
            index = (index + 1) % self.size

        # Found empty or deleted slot
        self.keys[index] = key
        self.values[index] = value
        self.flags[index] = 1  # Mark as occupied
        self.count += 1

    def search(self, key):
        """
        Search with lazy deletion handling
        """
        index = self._hash_function(key)
        start_index = index

        # Linear probing search
        for _ in range(self.size):
            if self.flags[index] == 0:  # Empty slot
                return None
            elif self.flags[index] == 1 and self.keys[index] == key:  # Found
                return self.values[index]

            index = (index + 1) % self.size
            if index == start_index:  # Checked all slots
                break

        return None

    def delete(self, key):
        """
        Lazy deletion: mark as deleted instead of removing
        """
        index = self._hash_function(key)
        start_index = index

        for _ in range(self.size):
            if self.flags[index] == 0:  # Empty slot, key not found
                return False
            elif self.flags[index] == 1 and self.keys[index] == key:  # Found
                # Lazy deletion
                self.flags[index] = 2  # Mark as deleted
                self.keys[index] = None
                self.values[index] = None
                self.count -= 1
                return True

            index = (index + 1) % self.size
            if index == start_index:
                break

        return False

    def _resize(self):
        """
        Efficient resizing with only occupied slots
        """
        old_size = self.size
        old_keys = self.keys.copy()
        old_values = self.values.copy()
        old_flags = self.flags.copy()

        # Double the size
        self.size = old_size * 2
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.flags = [0] * self.size
        self.count = 0

        print(f"Resizing advanced table from {old_size} to {self.size}")

        # Rehash only occupied slots
        for i in range(old_size):
            if old_flags[i] == 1:  # Only rehash occupied slots
                self.insert(old_keys[i], old_values[i])

    def display(self):
        """
        Display hash table with detailed information
        """
        print(f"\n{'=' * 60}")
        print(f"ADVANCED HASH TABLE")
        print(f"Size: {self.size}, Elements: {self.count}, Load Factor: {self.count / self.size:.2f}")
        print(f"{'=' * 60}")

        for i in range(self.size):
            if self.flags[i] == 0:
                status = "EMPTY"
                key_val = "-"
                value_val = "-"
            elif self.flags[i] == 1:
                status = "OCCUPIED"
                key_val = str(self.keys[i])
                value_val = str(self.values[i])
            else:  # flags[i] == 2
                status = "DELETED"
                key_val = "-"
                value_val = "-"

            print(f"Index {i:3}: [{status:9}] Key: {key_val:15} Value: {value_val:15}")

        print(f"{'=' * 60}")


# Example Usage and Demonstration
def demonstrate_basic_hash_table():
    """
    Demonstrate basic hash table operations with multiple inserts
    """
    print("\n" + "=" * 70)
    print("DEMONSTRATION 1: BASIC HASH TABLE WITH MULTIPLE INSERTS")
    print("=" * 70)

    # Create a small hash table to show collisions
    ht = HashTable(size=5)

    # Insert multiple values
    print("\n1. Inserting values:")
    ht.insert("apple", 10)
    ht.display()

    ht.insert("banana", 20)
    ht.display()

    ht.insert("orange", 30)
    ht.display()

    # This will cause collision and linear probing
    ht.insert("grape", 40)
    ht.display()

    # This will trigger resizing
    ht.insert("kiwi", 50)
    ht.display()

    # More inserts after resizing
    ht.insert("mango", 60)
    ht.insert("pear", 70)
    ht.insert("peach", 80)
    ht.display()

    # Demonstrate search
    print("\n2. Searching for values:")
    print(f"Search 'apple': {ht.search('apple')}")
    print(f"Search 'banana': {ht.search('banana')}")
    print(f"Search 'watermelon': {ht.search('watermelon')}")

    # Demonstrate update
    print("\n3. Updating existing key:")
    print("Before update - 'apple':", ht.search("apple"))
    ht.insert("apple", 100)  # Update value
    print("After update - 'apple':", ht.search("apple"))

    # Demonstrate deletion
    print("\n4. Deleting keys:")
    print("Delete 'banana':", ht.delete("banana"))
    ht.display()

    # Try to delete non-existent key
    print("Delete 'watermelon':", ht.delete("watermelon"))

    # Load factor
    print(f"\n5. Load Factor: {ht.get_load_factor():.2f}")


def demonstrate_collision_scenario():
    """
    Demonstrate how linear probing handles collisions
    """
    print("\n\n" + "=" * 70)
    print("DEMONSTRATION 2: COLLISION HANDLING WITH LINEAR PROBING")
    print("=" * 70)

    # Create very small table to force collisions
    ht = HashTable(size=4)

    # These keys will hash to different indices
    ht.insert("A", 1)  # Let's say hashes to index 0
    ht.insert("B", 2)  # Let's say hashes to index 1
    ht.insert("C", 3)  # Let's say hashes to index 2

    print("\nTable after inserting A, B, C:")
    ht.display()

    # Now insert a key that causes collision
    print("\nInserting 'D' (might cause collision):")
    ht.insert("D", 4)
    ht.display()

    # Show search with probing
    print("\nSearching for keys (shows probing path):")
    print("Search 'D':", ht.search("D"))

    # Show what happens when table is full
    print("\nTrying to insert 'E' (will trigger resize):")
    ht.insert("E", 5)
    ht.display()


def demonstrate_advanced_hash_table():
    """
    Demonstrate advanced hash table features
    """
    print("\n\n" + "=" * 70)
    print("DEMONSTRATION 3: ADVANCED HASH TABLE")
    print("=" * 70)

    aht = AdvancedHashTable(size=5)

    # Insert values
    aht.insert("John", 25)
    aht.insert("Alice", 30)
    aht.insert("Bob", 35)
    aht.insert("Eve", 28)
    aht.display()

    # Delete and show lazy deletion
    print("\nDeleting 'Alice':")
    aht.delete("Alice")
    aht.display()

    # Insert new value in deleted slot
    print("\nInserting 'Charlie' (may use deleted slot):")
    aht.insert("Charlie", 40)
    aht.display()

    # More operations
    print("\nUpdating 'Bob' to 36:")
    aht.insert("Bob", 36)
    aht.display()

    # Search operations
    print("\nSearch operations:")
    print(f"Search 'Bob': {aht.search('Bob')}")
    print(f"Search 'Alice' (deleted): {aht.search('Alice')}")
    print(f"Search 'David' (never inserted): {aht.search('David')}")


def performance_test():
    """
    Test performance with many inserts
    """
    print("\n\n" + "=" * 70)
    print("DEMONSTRATION 4: PERFORMANCE TEST WITH 1000 INSERTS")
    print("=" * 70)

    import time

    # Create hash table
    ht = HashTable(size=100)

    start_time = time.time()

    # Insert 1000 key-value pairs
    for i in range(1000):
        key = f"key_{i}"
        value = f"value_{i}"
        ht.insert(key, value)

    end_time = time.time()

    print(f"\nInserted 1000 elements in {end_time - start_time:.4f} seconds")
    print(f"Final table size: {ht.size}")
    print(f"Final element count: {ht.count}")
    print(f"Final load factor: {ht.get_load_factor():.2f}")

    # Search test
    print("\nSearch performance test:")
    start_time = time.time()
    for i in range(100):
        result = ht.search(f"key_{i * 10}")
    end_time = time.time()
    print(f"100 searches completed in {end_time - start_time:.6f} seconds")


def main():
    """
    Main function to run all demonstrations
    """
    # Run all demonstrations
    demonstrate_basic_hash_table()
    demonstrate_collision_scenario()
    demonstrate_advanced_hash_table()
    performance_test()

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
    Hash Table with Linear Probing:
    1. Uses array to store key-value pairs
    2. Hash function maps keys to array indices
    3. Linear probing handles collisions by checking next slot
    4. Dynamic resizing maintains performance
    5. O(1) average case, O(n) worst case for operations

    Key Concepts Demonstrated:
    - Collision resolution with linear probing
    - Dynamic resizing when load factor > threshold
    - Search with probing
    - Deletion strategies (simple vs lazy)
    - Performance with many elements
    """)


if __name__ == "__main__":
    main()