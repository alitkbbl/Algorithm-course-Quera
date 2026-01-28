from typing import Any, Optional, Iterator


class Node:
    """Node class for deque elements"""

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class Deque:
    """Complete Double-Ended Queue implementation with insert/remove at any position"""

    def __init__(self, iterable=None):
        """Initialize deque, optionally from an iterable"""
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None
        self.size: int = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def is_empty(self) -> bool:
        """Check if deque is empty"""
        return self.size == 0

    def __len__(self) -> int:
        """Return current size"""
        return self.size

    # === Basic Operations ===
    def append_left(self, data: Any) -> None:
        """Add element to front"""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def append(self, data: Any) -> None:
        """Add element to rear"""
        self.append_right(data)

    def append_right(self, data: Any) -> None:
        """Add element to rear"""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def pop_left(self) -> Any:
        """Remove and return front element"""
        if self.is_empty():
            raise IndexError("pop from empty deque")

        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data

    def pop(self) -> Any:
        """Remove and return rear element"""
        return self.pop_right()

    def pop_right(self) -> Any:
        """Remove and return rear element"""
        if self.is_empty():
            raise IndexError("pop from empty deque")

        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return data

    # === Advanced Operations ===
    def insert(self, index: int, data: Any) -> None:
        """
        Insert element at specified index
        Time Complexity: O(n) worst case
        """
        if index < 0:
            index = self.size + index + 1

        if index <= 0:
            self.append_left(data)
        elif index >= self.size:
            self.append_right(data)
        else:
            # Insert in the middle
            new_node = Node(data)
            current = self.front

            # Traverse to position before insertion
            for _ in range(index - 1):
                current = current.next

            # Insert new node
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.size += 1

    def remove(self, data: Any) -> None:
        """
        Remove first occurrence of data
        Time Complexity: O(n)
        """
        current = self.front
        while current:
            if current.data == data:
                if current == self.front:
                    self.pop_left()
                elif current == self.rear:
                    self.pop_right()
                else:
                    # Remove from middle
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                return
            current = current.next
        raise ValueError(f"{data} not found in deque")

    def remove_at(self, index: int) -> Any:
        """
        Remove and return element at specified index
        Time Complexity: O(n)
        """
        if index < 0:
            index = self.size + index

        if index < 0 or index >= self.size:
            raise IndexError("index out of range")

        if index == 0:
            return self.pop_left()
        elif index == self.size - 1:
            return self.pop_right()
        else:
            current = self.front
            for _ in range(index):
                current = current.next

            # Remove middle node
            data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return data

    def extend(self, iterable) -> None:
        """Add all elements from iterable to rear"""
        for item in iterable:
            self.append(item)

    def extend_left(self, iterable) -> None:
        """Add all elements from iterable to front (in reverse order)"""
        for item in reversed(list(iterable)):
            self.append_left(item)

    def rotate(self, n: int = 1) -> None:
        """
        Rotate deque n steps to the right (positive n)
        or to the left (negative n)
        """
        if self.size <= 1:
            return

        n = n % self.size
        if n == 0:
            return

        if n > 0:
            # Rotate right
            for _ in range(n):
                self.append_left(self.pop_right())
        else:
            # Rotate left
            for _ in range(-n):
                self.append_right(self.pop_left())

    # === Access Operations ===
    def peek_left(self) -> Any:
        """Get front element without removing"""
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.front.data

    def peek_right(self) -> Any:
        """Get rear element without removing"""
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.rear.data

    def get(self, index: int) -> Any:
        """Get element at index without removing"""
        if index < 0:
            index = self.size + index

        if index < 0 or index >= self.size:
            raise IndexError("index out of range")

        current = self.front
        for _ in range(index):
            current = current.next
        return current.data

    def index(self, data: Any, start: int = 0, end: Optional[int] = None) -> int:
        """
        Return first index of data
        Raises ValueError if not found
        """
        if end is None:
            end = self.size

        current = self.front
        for i in range(self.size):
            if i >= start and i < end:
                if current.data == data:
                    return i
            current = current.next
        raise ValueError(f"{data} not found in deque")

    def count(self, data: Any) -> int:
        """Count occurrences of data"""
        count = 0
        current = self.front
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    # === Utility Methods ===
    def clear(self) -> None:
        """Remove all elements"""
        self.front = self.rear = None
        self.size = 0

    def copy(self) -> 'Deque':
        """Return a shallow copy"""
        new_deque = Deque()
        current = self.front
        while current:
            new_deque.append(current.data)
            current = current.next
        return new_deque

    def reverse(self) -> None:
        """Reverse deque in place"""
        if self.size <= 1:
            return

        current = self.front
        while current:
            # Swap next and prev pointers
            current.next, current.prev = current.prev, current.next
            current = current.prev

        # Swap front and rear
        self.front, self.rear = self.rear, self.front

    # === Python Special Methods ===
    def __contains__(self, data: Any) -> bool:
        current = self.front
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __iter__(self) -> Iterator[Any]:
        current = self.front
        while current:
            yield current.data
            current = current.next

    def __reversed__(self) -> Iterator[Any]:
        current = self.rear
        while current:
            yield current.data
            current = current.prev

    def __str__(self) -> str:
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Deque([" + ", ".join(elements) + "])"

    def __repr__(self) -> str:
        return f"Deque(size={self.size})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Deque):
            return False
        if len(self) != len(other):
            return False
        return all(a == b for a, b in zip(self, other))


# ==================== COMPREHENSIVE TEST SUITE ====================

def run_comprehensive_tests():
    """Run comprehensive tests for all deque operations"""

    print("=" * 60)
    print("COMPREHENSIVE DEQUE TEST SUITE")
    print("=" * 60)

    # Test 1: Basic Operations
    print("\n1. BASIC OPERATIONS")
    print("-" * 40)

    dq = Deque()
    print(f"Initial deque: {dq}")
    print(f"Is empty? {dq.is_empty()}")

    # Append operations
    dq.append(10)  # [10]
    dq.append_left(5)  # [5, 10]
    dq.append_right(15)  # [5, 10, 15]
    print(f"After appends: {dq}")
    print(f"Size: {len(dq)}")

    # Pop operations
    print(f"\nPop left: {dq.pop_left()}")  # Removes 5
    print(f"After pop_left: {dq}")  # [10, 15]
    print(f"Pop right: {dq.pop_right()}")  # Removes 15
    print(f"After pop_right: {dq}")  # [10]
    print(f"Pop: {dq.pop()}")  # Removes 10 (alias for pop_right)
    print(f"After all pops: {dq}")  # []

    # Test 2: Insert Operations
    print("\n\n2. INSERT OPERATIONS")
    print("-" * 40)

    dq = Deque([1, 2, 3])
    print(f"Initial: {dq}")  # [1, 2, 3]

    dq.insert(0, 0)  # Insert at beginning
    print(f"insert(0, 0): {dq}")  # [0, 1, 2, 3]

    dq.insert(2, 1.5)  # Insert in middle
    print(f"insert(2, 1.5): {dq}")  # [0, 1, 1.5, 2, 3]

    dq.insert(5, 4)  # Insert at end
    print(f"insert(5, 4): {dq}")  # [0, 1, 1.5, 2, 3, 4]

    dq.insert(-1, 3.5)  # Insert before last
    print(f"insert(-1, 3.5): {dq}")  # [0, 1, 1.5, 2, 3, 3.5, 4]

    # Test 3: Remove Operations
    print("\n\n3. REMOVE OPERATIONS")
    print("-" * 40)

    dq = Deque([10, 20, 30, 20, 40])
    print(f"Initial: {dq}")  # [10, 20, 30, 20, 40]

    dq.remove(20)  # Remove first 20
    print(f"remove(20): {dq}")  # [10, 30, 20, 40]

    print(f"remove_at(2): {dq.remove_at(2)}")  # Remove at index 2
    print(f"After remove_at(2): {dq}")  # [10, 30, 40]

    try:
        dq.remove(99)  # Should raise ValueError
    except ValueError as e:
        print(f"Expected error remove(99): {e}")

    # Test 4: Extend and Rotate
    print("\n\n4. EXTEND AND ROTATE")
    print("-" * 40)

    dq1 = Deque([1, 2])
    dq2 = Deque([3, 4])

    dq1.extend(dq2)
    print(f"extend([3, 4]): {dq1}")  # [1, 2, 3, 4]

    dq1.extend_left([0, -1])
    print(f"extend_left([0, -1]): {dq1}")  # [-1, 0, 1, 2, 3, 4]

    dq1.rotate(2)
    print(f"rotate(2): {dq1}")  # [3, 4, -1, 0, 1, 2]

    dq1.rotate(-1)
    print(f"rotate(-1): {dq1}")  # [4, -1, 0, 1, 2, 3]

    # Test 5: Access Methods
    print("\n\n5. ACCESS METHODS")
    print("-" * 40)

    dq = Deque([5, 10, 15, 20, 25])
    print(f"Deque: {dq}")

    print(f"peek_left(): {dq.peek_left()}")  # 5
    print(f"peek_right(): {dq.peek_right()}")  # 25
    print(f"get(2): {dq.get(2)}")  # 15
    print(f"get(-1): {dq.get(-1)}")  # 25

    print(f"index(15): {dq.index(15)}")  # 2
    print(f"index(20, 2): {dq.index(20, 2)}")  # 3
    print(f"count(10): {dq.count(10)}")  # 1

    # Test 6: Utility Methods
    print("\n\n6. UTILITY METHODS")
    print("-" * 40)

    dq = Deque([1, 2, 3, 4, 5])
    print(f"Original: {dq}")

    dq_copy = dq.copy()
    print(f"Copy: {dq_copy}")

    dq.reverse()
    print(f"After reverse(): {dq}")  # [5, 4, 3, 2, 1]

    dq.clear()
    print(f"After clear(): {dq}")
    print(f"Is empty? {dq.is_empty()}")

    # Test 7: Iterator and Contains
    print("\n\n7. ITERATOR AND CONTAINS")
    print("-" * 40)

    dq = Deque(['a', 'b', 'c', 'd'])
    print(f"Deque: {dq}")

    print("Forward iteration:")
    for item in dq:
        print(f"  {item}")

    print("Reverse iteration:")
    for item in reversed(dq):
        print(f"  {item}")

    print(f"'b' in deque: {'b' in dq}")  # True
    print(f"'z' in deque: {'z' in dq}")  # False

    # Test 8: Initialization from Iterable
    print("\n\n8. INITIALIZATION FROM ITERABLE")
    print("-" * 40)

    dq1 = Deque(range(5))
    print(f"Deque(range(5)): {dq1}")

    dq2 = Deque([1, 2, 3])
    print(f"Deque([1, 2, 3]): {dq2}")

    dq3 = Deque("hello")
    print(f"Deque('hello'): {dq3}")

    # Test 9: Edge Cases
    print("\n\n9. EDGE CASES")
    print("-" * 40)

    # Empty deque operations
    empty_dq = Deque()
    print(f"Empty deque: {empty_dq}")
    print(f"Is empty? {empty_dq.is_empty()}")

    try:
        empty_dq.pop_left()
    except IndexError as e:
        print(f"Expected error pop_left(): {e}")

    # Single element deque
    single_dq = Deque([42])
    print(f"\nSingle element deque: {single_dq}")
    print(f"peek_left: {single_dq.peek_left()}")
    print(f"peek_right: {single_dq.peek_right()}")

    single_dq.pop()
    print(f"After pop: {single_dq}")

    # Test 10: Equality Test
    print("\n\n10. EQUALITY TEST")
    print("-" * 40)

    dq1 = Deque([1, 2, 3])
    dq2 = Deque([1, 2, 3])
    dq3 = Deque([1, 2, 4])

    print(f"dq1 == dq2: {dq1 == dq2}")  # True
    print(f"dq1 == dq3: {dq1 == dq3}")  # False

    # Test 11: Performance Demo
    print("\n\n11. PERFORMANCE DEMO")
    print("-" * 40)

    # Creating large deque
    print("Creating deque with 10000 elements...")
    large_dq = Deque(range(10000))
    print(f"Size: {len(large_dq)}")

    # Fast operations at ends
    print("\nFast end operations:")
    import time

    start = time.time()
    large_dq.append_left(-1)
    large_dq.append(10000)
    end = time.time()
    print(f"Two end operations: {(end - start) * 1000:.6f} ms")

    # Slower middle operations
    print("\nMiddle operations (slower):")
    start = time.time()
    large_dq.insert(5000, "middle")
    end = time.time()
    print(f"Insert at middle: {(end - start) * 1000:.6f} ms")

    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)


def real_world_examples():
    """Show real-world use cases"""

    print("\n\n" + "=" * 60)
    print("REAL-WORLD EXAMPLES")
    print("=" * 60)

    # Example 1: Sliding Window Maximum
    print("\n1. SLIDING WINDOW MAXIMUM")
    print("-" * 40)

    def sliding_window_max(nums, k):
        """Find max in each sliding window of size k"""
        dq = Deque()
        result = []

        for i, num in enumerate(nums):
            # Remove elements outside window
            if dq and dq.peek_left() <= i - k:
                dq.pop_left()

            # Remove smaller elements from back
            while dq and nums[dq.peek_right()] <= num:
                dq.pop_right()

            dq.append(i)

            # Add max to result
            if i >= k - 1:
                result.append(nums[dq.peek_left()])

        return result

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Array: {nums}")
    print(f"Window size: {k}")
    print(f"Sliding window max: {sliding_window_max(nums, k)}")

    # Example 2: Palindrome Checker
    print("\n2. PALINDROME CHECKER")
    print("-" * 40)

    def is_palindrome(word):
        dq = Deque(word.lower())
        while len(dq) > 1:
            if dq.pop_left() != dq.pop_right():
                return False
        return True

    test_words = ["radar", "hello", "A man a plan a canal Panama", "racecar"]
    for word in test_words:
        clean_word = ''.join(ch for ch in word.lower() if ch.isalnum())
        print(f"'{word}' is palindrome? {is_palindrome(clean_word)}")

    # Example 3: Task Scheduler
    print("\n3. TASK SCHEDULER")
    print("-" * 40)

    class TaskScheduler:
        def __init__(self):
            self.tasks = Deque()

        def add_task(self, task, priority="normal"):
            if priority == "high":
                self.tasks.append_left(task)
            else:
                self.tasks.append(task)

        def process_tasks(self):
            while self.tasks:
                task = self.tasks.pop_left()
                print(f"Processing: {task}")

    scheduler = TaskScheduler()
    scheduler.add_task("Backup database")
    scheduler.add_task("Send email report", "high")
    scheduler.add_task("Generate report")
    scheduler.add_task("System check", "high")

    print("Task processing order:")
    scheduler.process_tasks()


if __name__ == "__main__":
    # Run all tests
    run_comprehensive_tests()

    # Show real-world examples
    real_world_examples()

    # Quick comparison with Python's deque
    print("\n\n" + "=" * 60)
    print("COMPARISON WITH PYTHON'S collections.deque")
    print("=" * 60)

    from collections import deque as py_deque

    print("\nPython's deque:")
    py_dq = py_deque([1, 2, 3])
    py_dq.appendleft(0)
    py_dq.append(4)
    print(f"After operations: {list(py_dq)}")

    print("\nOur Deque:")
    our_dq = Deque([1, 2, 3])
    our_dq.append_left(0)
    our_dq.append(4)
    print(f"After same operations: {our_dq}")