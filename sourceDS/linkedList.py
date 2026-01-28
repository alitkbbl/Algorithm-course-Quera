class Node:
    """Node class for linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Singly Linked List Implementation"""

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty List"

    def is_empty(self):
        return self.head is None

    # Insert at the beginning (prepend)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return new_node

    # Insert at the end (append)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.size += 1
        return new_node

    # Insert at specific position (0-indexed)
    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            raise IndexError(f"Position {position} out of bounds")

        if position == 0:
            return self.insert_at_beginning(data)

        if position == self.size:
            return self.insert_at_end(data)

        new_node = Node(data)
        current = self.head

        # Move to the node before the insertion point
        for _ in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return new_node

    # Insert in sorted order (assuming the list is sorted)
    def insert_sorted(self, data):
        new_node = Node(data)

        # If list is empty or new node should be at the beginning
        if self.is_empty() or self.head.data >= data:
            return self.insert_at_beginning(data)

        current = self.head

        # Find the position to insert
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return new_node

    # Insert multiple keys using various methods
    def insert_keys(self, keys, method="end"):
        """
        Insert multiple keys into the linked list

        Parameters:
        - keys: list of values to insert
        - method: "beginning", "end", "sorted", or "position"
                  (for position method, inserts at positions 0, 1, 2, ...)
        """
        if method == "beginning":
            for key in keys:
                self.insert_at_beginning(key)

        elif method == "end":
            for key in keys:
                self.insert_at_end(key)

        elif method == "sorted":
            for key in keys:
                self.insert_sorted(key)

        elif method == "position":
            for i, key in enumerate(keys):
                self.insert_at_position(key, i)

        else:
            raise ValueError(f"Unknown insertion method: {method}")

        return self

    # Search for a value
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    # Get value at position
    def get_at_position(self, position):
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} out of bounds")

        current = self.head
        for _ in range(position):
            current = current.next
        return current.data

    # Delete by value
    def delete(self, data):
        if self.is_empty():
            return False

        # If head needs to be deleted
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        return self


# Example usage with your keys
if __name__ == "__main__":
    insert_keys = [40, 20, 60, 10, 30, 50, 70, 25, 27, 26, 5, 15, 65, 80, 75]

    print("=" * 60)
    print("LINKED LIST DEMONSTRATION")
    print("=" * 60)

    # Test 1: Insert at the end (default behavior)
    print("\n1. Inserting keys at the END of the list:")
    ll1 = LinkedList()
    ll1.insert_keys(insert_keys, method="end")
    print(f"Linked List: {ll1}")
    print(f"Size: {len(ll1)}")

    # Test 2: Insert at the beginning
    print("\n2. Inserting keys at the BEGINNING of the list:")
    ll2 = LinkedList()
    ll2.insert_keys(insert_keys, method="beginning")
    print(f"Linked List: {ll2}")
    print(f"Size: {len(ll2)}")

    # Test 3: Insert in sorted order
    print("\n3. Inserting keys in SORTED order:")
    ll3 = LinkedList()
    ll3.insert_keys(insert_keys, method="sorted")
    print(f"Linked List: {ll3}")
    print(f"Size: {len(ll3)}")

    # Test 4: Insert at specific positions
    print("\n4. Inserting keys at POSITIONS 0, 1, 2, ...:")
    ll4 = LinkedList()
    ll4.insert_keys(insert_keys[:5], method="position")
    print(f"Linked List (first 5 keys): {ll4}")
    print(f"Size: {len(ll4)}")

    # Test 5: Search for values
    print("\n5. Searching for values in the sorted list:")
    search_values = [30, 75, 100]
    for value in search_values:
        position = ll3.search(value)
        if position != -1:
            print(f"Value {value} found at position {position}")
        else:
            print(f"Value {value} not found in the list")

    # Test 6: Reverse the list
    print("\n6. Reversing the list (using first list):")
    print(f"Original: {ll1}")
    ll1.reverse()
    print(f"Reversed: {ll1}")

    # Test 7: Delete operations
    print("\n7. Deleting values from the sorted list:")
    print(f"Before deletion: {ll3}")

    to_delete = [30, 75, 10]
    for value in to_delete:
        if ll3.delete(value):
            print(f"Deleted {value}: {ll3}")
        else:
            print(f"Could not delete {value}, not found")

    print(f"Final list: {ll3}")
    print(f"Size: {len(ll3)}")

    # Test 8: Get value at position
    print("\n8. Getting values at specific positions:")
    positions = [0, 5, len(ll3)-1]
    for pos in positions:
        try:
            value = ll3.get_at_position(pos)
            print(f"Position {pos}: {value}")
        except IndexError as e:
            print(f"Error: {e}")

    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)