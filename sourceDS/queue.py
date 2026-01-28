from typing import Any, Optional


class ListQueue:
    """
    Queue implementation using Python list
    Note: This is inefficient for large queues due to O(n) pop(0) operation
    """

    def __init__(self):
        """Initialize an empty queue"""
        self._items = []

    def enqueue(self, item: Any) -> None:
        """Add item to the back of the queue"""
        self._items.append(item)  # O(1)

    def dequeue(self) -> Optional[Any]:
        """Remove and return item from the front of the queue"""
        if self.is_empty():
            return None
        return self._items.pop(0)  # O(n) - inefficient!

    def front(self) -> Optional[Any]:
        """Return item at the front without removing it"""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return len(self._items) == 0

    def size(self) -> int:
        """Return number of items in queue"""
        return len(self._items)

    def __str__(self) -> str:
        """String representation of queue"""
        if self.is_empty():
            return "Empty Queue"
        return f"Queue({self._items})"


# Test the ListQueue
def test_list_queue():
    """Test function for ListQueue implementation"""
    print("\nTesting ListQueue Implementation")
    print("=" * 40)

    queue = ListQueue()

    # Test basic operations
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(f"Queue: {queue}")
    print(f"Front: {queue.front()}")
    print(f"Size: {queue.size()}")

    print(f"Dequeue: {queue.dequeue()}")
    print(f"After dequeue: {queue}")
    print(f"Is empty? {queue.is_empty()}")


# Run the test
if __name__ == "__main__":
    test_list_queue()