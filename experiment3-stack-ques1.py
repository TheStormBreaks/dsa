class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

def reverse_myname(name):
    stack = Stack()

    # Push all characters of the name onto the stack
    for char in name:
        stack.push(char)

    # Pop all characters from the stack and form the reversed string
    reversed_name = ""
    while not stack.is_empty():
        reversed_name += stack.pop()

    return reversed_name

# Example usage
name = "Jayce Arcane"
reversed_name = reverse_myname(name)
print("Original Name:", name)
print("Reversed Name:", reversed_name)
