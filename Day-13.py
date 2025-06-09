class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed {item} → Stack: {self.items}")

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            popped = self.items.pop()
            print(f"Popped {popped} → Stack: {self.items}")
            return popped
        print("Stack is empty. Nothing to pop.")
        return None

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            print(f"Top item is: {self.items[-1]}")
            return self.items[-1]
        print("Stack is empty. Nothing to peek.")
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)                                                                               #When someone prints this object (e.g., print(stack)), show it as a string version of self.items.


stack = Stack()

# Push some numbers
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

# Peek at the top
stack.peek()

# Pop a few elements
stack.pop()
stack.pop()

# Push again
stack.push(50)
stack.push(60)

# Peek again
stack.peek()

# Final pops
stack.pop()
stack.pop()
stack.pop()
stack.pop()

# One more peek just to show it's empty
stack.peek()




