class Stack:
    def __init__(self, max_size=None):
        """
        Initialize a Stack

        Args:
            max_size: Maximum size of stack (optional)
        """
        self.items = []  # Using Python list as underlying storage
        self.max_size = max_size
        self.top = -1  # Index of top element (-1 means empty)

        print(f"✓ Stack created successfully!")
        if max_size:
            print(f"  Maximum size: {max_size}")
        else:
            print(f"  Unlimited size")

    def push(self, item):
        """
        Push an item onto the stack

        Args:
            item: Item to push

        Returns:
            True if successful, False if stack is full
        """
        print(f"\n{'=' * 40}")
        print(f"PUSH OPERATION: {item}")
        print(f"{'=' * 40}")

        # Check if stack is full (if max_size is set)
        if self.max_size is not None and self.is_full():
            print(f"✗ STACK OVERFLOW! Cannot push {item}")
            print(f"  Stack is full (max size: {self.max_size})")
            return False

        # Push the item
        self.items.append(item)
        self.top += 1

        print(f"✓ Pushed {item} onto stack")
        print(f"  Stack after push: {self}")
        print(f"  Top index: {self.top}")
        print(f"  Stack size: {len(self)}")

        return True

    def pop(self):
        """
        Pop an item from the stack

        Returns:
            Popped item if successful, None if stack is empty
        """
        print(f"\n{'=' * 40}")
        print(f"POP OPERATION")
        print(f"{'=' * 40}")

        # Check if stack is empty
        if self.is_empty():
            print(f"✗ STACK UNDERFLOW! Cannot pop from empty stack")
            return None

        # Pop the item
        item = self.items.pop()
        self.top -= 1

        print(f"✓ Popped {item} from stack")
        print(f"  Stack after pop: {self}")
        print(f"  Top index: {self.top}")
        print(f"  Stack size: {len(self)}")

        return item

    def peek(self):
        """
        Peek at the top item without removing it

        Returns:
            Top item if stack not empty, None otherwise
        """
        print(f"\n{'=' * 40}")
        print(f"PEEK OPERATION")
        print(f"{'=' * 40}")

        if self.is_empty():
            print(f"✗ Stack is empty, nothing to peek")
            return None

        item = self.items[self.top]
        print(f"✓ Top item is: {item}")
        print(f"  Stack remains unchanged: {self}")

        return item

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def is_full(self):
        """Check if stack is full (only if max_size is set)"""
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size

    def size(self):
        """Get current stack size"""
        return len(self.items)

    def clear(self):
        """Clear all items from stack"""
        print(f"\n{'=' * 40}")
        print(f"CLEAR OPERATION")
        print(f"{'=' * 40}")

        if self.is_empty():
            print(f"Stack is already empty")
            return

        old_size = len(self.items)
        self.items.clear()
        self.top = -1

        print(f"✓ Cleared all {old_size} items from stack")
        print(f"  Stack is now empty")

    def search(self, item):
        """
        Search for an item in the stack

        Args:
            item: Item to search for

        Returns:
            Position from top (1-based) if found, -1 otherwise
        """
        print(f"\n{'=' * 40}")
        print(f"SEARCH OPERATION: {item}")
        print(f"{'=' * 40}")

        if self.is_empty():
            print(f"✗ Stack is empty, cannot search")
            return -1

        # Search from top (end of list) downwards
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == item:
                position_from_top = len(self.items) - i
                print(f"✓ Found {item} at position {position_from_top} from top")
                print(f"  Stack (top to bottom): {self}")
                return position_from_top

        print(f"✗ Item {item} not found in stack")
        return -1

    def display(self):
        """Display stack contents visually"""
        print(f"\n{'=' * 40}")
        print(f"STACK DISPLAY")
        print(f"{'=' * 40}")

        if self.is_empty():
            print("┌─────────────────┐")
            print("│     EMPTY       │")
            print("└─────────────────┘")
            return

        # Get max width for formatting
        max_item_width = max(len(str(item)) for item in self.items)
        max_item_width = max(max_item_width, 6)  # Minimum width

        border = "─" * (max_item_width + 4)

        print(f"Size: {len(self)} | Top index: {self.top}")
        print(f"Top → Bottom:")

        # Display from top to bottom
        for i in range(len(self.items) - 1, -1, -1):
            item = self.items[i]
            item_str = str(item).center(max_item_width)

            if i == self.top:
                print(f"┌{border}┐")
                print(f"│  {item_str}  │ ← TOP")
                print(f"└{border}┘")
            else:
                print(f"│  {item_str}  │")

        if not self.is_empty():
            print(f"  ↑")
            print(f"BOTTOM")

    def reverse(self):
        """Reverse the stack (using another stack)"""
        print(f"\n{'=' * 40}")
        print(f"REVERSE OPERATION")
        print(f"{'=' * 40}")

        if self.is_empty():
            print(f"Stack is empty, nothing to reverse")
            return

        print(f"Original stack: {self}")

        # Create a temporary stack
        temp_stack = Stack()

        # Reverse using push/pop
        while not self.is_empty():
            temp_stack.push(self.pop())

        # Now temp_stack has reversed order
        # We need to create another temp to get correct order
        final_stack = Stack()
        while not temp_stack.is_empty():
            final_stack.push(temp_stack.pop())

        # Replace our stack with the reversed one
        self.items = final_stack.items
        self.top = len(self.items) - 1

        print(f"Reversed stack: {self}")

    def __len__(self):
        """Get stack size using len()"""
        return len(self.items)

    def __str__(self):
        """String representation of stack (top to bottom)"""
        if self.is_empty():
            return "[]"

        # Show from top to bottom
        items_str = [str(item) for item in reversed(self.items)]
        return "[" + " ← ".join(items_str) + "]"

    def __repr__(self):
        """Official string representation"""
        return f"Stack({self.items})"

    def __contains__(self, item):
        """Check if item is in stack using 'in' operator"""
        return item in self.items


# Advanced Stack with array implementation (for fixed size)
class ArrayStack:
    def __init__(self, capacity=10):
        """
        Initialize a Stack using fixed-size array

        Args:
            capacity: Fixed capacity of stack
        """
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1  # Index of top element

        print(f"✓ ArrayStack created with capacity {capacity}")

    def push(self, item):
        """Push item onto stack"""
        if self.is_full():
            print(f"✗ STACK OVERFLOW! Cannot push {item}")
            return False

        self.top += 1
        self.array[self.top] = item
        print(f"✓ Pushed {item} at index {self.top}")
        return True

    def pop(self):
        """Pop item from stack"""
        if self.is_empty():
            print(f"✗ STACK UNDERFLOW! Cannot pop")
            return None

        item = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        print(f"✓ Popped {item}")
        return item

    def peek(self):
        """Peek at top item"""
        if self.is_empty():
            return None
        return self.array[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

    def display(self):
        """Display array-based stack"""
        print(f"\nArrayStack (capacity: {self.capacity}):")
        print("Index | Value")
        print("-" * 20)

        for i in range(self.capacity - 1, -1, -1):
            arrow = " ← TOP" if i == self.top else ""
            value = self.array[i] if i <= self.top and self.array[i] is not None else ""
            print(f"{i:5} | {value} {arrow}")

        print(f"Top index: {self.top}, Size: {self.size()}")


# Stack Applications
class StackApplications:
    @staticmethod
    def check_parentheses(expression):
        """
        Check if parentheses in expression are balanced

        Args:
            expression: String expression to check

        Returns:
            True if balanced, False otherwise
        """
        print(f"\n{'=' * 60}")
        print(f"PARENTHESES CHECK: {expression}")
        print(f"{'=' * 60}")

        stack = Stack()
        opening = "({["
        closing = ")}]"

        print("Step-by-step checking:")

        for i, char in enumerate(expression):
            print(f"\nCharacter {i + 1}: '{char}'")

            if char in opening:
                print(f"  Pushing opening parenthesis '{char}'")
                stack.push(char)
                print(f"  Stack: {stack}")
            elif char in closing:
                if stack.is_empty():
                    print(f"  ✗ Found closing '{char}' but stack is empty")
                    print(f"  UNBALANCED: Too many closing parentheses")
                    return False

                top = stack.peek()
                print(f"  Found closing '{char}', top of stack is '{top}'")

                # Check if parentheses match
                if opening.index(top) == closing.index(char):
                    popped = stack.pop()
                    print(f"  ✓ Matched! Popped '{popped}'")
                    print(f"  Stack: {stack}")
                else:
                    print(f"  ✗ Mismatch! Expected '{closing[opening.index(top)]}' but found '{char}'")
                    return False

        is_balanced = stack.is_empty()

        if is_balanced:
            print(f"\n✓ EXPRESSION IS BALANCED!")
        else:
            print(f"\n✗ EXPRESSION IS UNBALANCED!")
            print(f"  Stack not empty: {stack}")
            print(f"  Too many opening parentheses")

        return is_balanced

    @staticmethod
    def decimal_to_binary(decimal_num):
        """
        Convert decimal number to binary using stack

        Args:
            decimal_num: Decimal number to convert

        Returns:
            Binary string
        """
        print(f"\n{'=' * 60}")
        print(f"DECIMAL TO BINARY CONVERSION: {decimal_num}")
        print(f"{'=' * 60}")

        if decimal_num == 0:
            return "0"

        stack = Stack()
        num = decimal_num

        print("Division process:")
        while num > 0:
            remainder = num % 2
            print(f"  {num} ÷ 2 = {num // 2} remainder {remainder}")
            stack.push(remainder)
            num = num // 2

        print(f"\nStack after divisions: {stack}")

        # Build binary string by popping from stack
        binary_str = ""
        print("\nReading remainders from stack (reverse order):")
        while not stack.is_empty():
            bit = stack.pop()
            binary_str += str(bit)
            print(f"  Popped {bit} → Binary so far: {binary_str}")

        print(f"\n✓ Final binary: {binary_str}")
        return binary_str

    @staticmethod
    def reverse_string(input_str):
        """
        Reverse a string using stack

        Args:
            input_str: String to reverse

        Returns:
            Reversed string
        """
        print(f"\n{'=' * 60}")
        print(f"STRING REVERSAL: '{input_str}'")
        print(f"{'=' * 60}")

        stack = Stack()

        print("Pushing characters onto stack:")
        for char in input_str:
            print(f"  Pushing '{char}'")
            stack.push(char)

        print(f"\nStack after pushing: {stack}")

        reversed_str = ""
        print("\nPopping characters from stack (reverse order):")
        while not stack.is_empty():
            char = stack.pop()
            reversed_str += char
            print(f"  Popped '{char}' → Reversed so far: '{reversed_str}'")

        print(f"\n✓ Original: '{input_str}'")
        print(f"✓ Reversed: '{reversed_str}'")

        return reversed_str

    @staticmethod
    def evaluate_postfix(expression):
        """
        Evaluate postfix (Reverse Polish Notation) expression

        Args:
            expression: Postfix expression string

        Returns:
            Result of evaluation
        """
        print(f"\n{'=' * 60}")
        print(f"POSTFIX EVALUATION: {expression}")
        print(f"{'=' * 60}")

        stack = Stack()
        tokens = expression.split()

        print("Step-by-step evaluation:")

        for token in tokens:
            print(f"\nToken: '{token}'")

            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                # It's a number
                num = int(token)
                stack.push(num)
                print(f"  Pushed number: {num}")
                print(f"  Stack: {stack}")
            else:
                # It's an operator
                if stack.size() < 2:
                    print(f"  ✗ Error: Not enough operands for operator '{token}'")
                    return None

                operand2 = stack.pop()
                operand1 = stack.pop()

                print(f"  Popped operands: {operand1} and {operand2}")

                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    if operand2 == 0:
                        print(f"  ✗ Error: Division by zero")
                        return None
                    result = operand1 / operand2
                elif token == '^':
                    result = operand1 ** operand2
                else:
                    print(f"  ✗ Error: Unknown operator '{token}'")
                    return None

                print(f"  Operation: {operand1} {token} {operand2} = {result}")
                stack.push(result)
                print(f"  Pushed result: {result}")
                print(f"  Stack: {stack}")

        if stack.size() != 1:
            print(f"\n✗ Error: Invalid expression")
            return None

        final_result = stack.pop()
        print(f"\n✓ Final result: {final_result}")
        return final_result


# Test Stack Implementation
if __name__ == "__main__":
    print("STACK DATA STRUCTURE DEMONSTRATION")
    print("=" * 60)

    # Create stacks
    print("\n1. CREATING STACKS")
    print("-" * 40)

    unlimited_stack = Stack()
    limited_stack = Stack(max_size=5)
    array_stack = ArrayStack(capacity=5)

    # Test basic operations
    print("\n\n2. BASIC STACK OPERATIONS (Unlimited Stack)")
    print("-" * 40)

    test_items = [10, 20, 30, 40, 50]

    for item in test_items:
        unlimited_stack.push(item)

    unlimited_stack.display()
    unlimited_stack.peek()
    unlimited_stack.pop()
    unlimited_stack.peek()
    unlimited_stack.display()

    # Test limited stack
    print("\n\n3. LIMITED STACK (Max Size: 5)")
    print("-" * 40)

    for item in [1, 2, 3, 4, 5, 6]:  # 6th should cause overflow
        limited_stack.push(item)

    limited_stack.display()

    # Test search
    print("\n\n4. SEARCH OPERATIONS")
    print("-" * 40)

    unlimited_stack.search(20)
    unlimited_stack.search(100)

    # Test clear
    print("\n\n5. CLEAR OPERATION")
    print("-" * 40)

    unlimited_stack.clear()
    unlimited_stack.display()

    # Test reverse
    print("\n\n6. REVERSE OPERATION")
    print("-" * 40)

    unlimited_stack.push(1)
    unlimited_stack.push(2)
    unlimited_stack.push(3)
    unlimited_stack.display()
    unlimited_stack.reverse()
    unlimited_stack.display()

    # Test array-based stack
    print("\n\n7. ARRAY-BASED STACK")
    print("-" * 40)

    array_stack.push('A')
    array_stack.push('B')
    array_stack.push('C')
    array_stack.display()
    array_stack.pop()
    array_stack.display()

    # Test stack applications
    print("\n\n8. STACK APPLICATIONS")
    print("-" * 40)

    app = StackApplications()

    # Parentheses checking
    expressions = [
        "((2 + 3) * 5)",
        "{[()]}",
        "((2 + 3) * 5",
        "([)]",
        ""
    ]

    for expr in expressions:
        app.check_parentheses(expr)
        print()

    # Decimal to binary
    numbers = [10, 42, 255, 0, 1]
    for num in numbers:
        app.decimal_to_binary(num)
        print()

    # String reversal
    strings = ["hello", "Python", "racecar", "a", ""]
    for s in strings:
        app.reverse_string(s)
        print()

    # Postfix evaluation
    postfix_expressions = [
        "5 3 +",  # 5 + 3 = 8
        "5 3 2 * +",  # 5 + (3 * 2) = 11
        "10 2 / 3 +",  # (10 / 2) + 3 = 8
        "2 3 ^ 4 +",  # 2^3 + 4 = 12
        "5 0 /"  # Error: division by zero
    ]

    for expr in postfix_expressions:
        app.evaluate_postfix(expr)
        print()

    # Edge cases
    print("\n\n9. EDGE CASES")
    print("-" * 40)

    empty_stack = Stack()
    empty_stack.pop()
    empty_stack.peek()
    empty_stack.display()

    # Test __contains__
    test_stack = Stack()
    test_stack.push(100)
    test_stack.push(200)
    print(f"\nIs 100 in stack? {100 in test_stack}")
    print(f"Is 300 in stack? {300 in test_stack}")

    # Test len()
    print(f"\nStack size using len(): {len(test_stack)}")

    # Memory efficient operations
    print("\n\n10. MEMORY EFFICIENT OPERATIONS")
    print("-" * 40)

    print("\nUsing multiple pops:")
    test_stack.push(300)
    test_stack.push(400)
    test_stack.push(500)
    test_stack.display()

    print("\nPopping 3 items:")
    for i in range(3):
        test_stack.pop()
    test_stack.display()