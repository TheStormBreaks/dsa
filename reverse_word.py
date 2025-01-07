class Stack:
    def __init__(self):
        self.items = []

    # Push an element onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0





#LOGIC PART
# Function to reverse a word using a stack
def rev(word):
    stack = Stack()
    
    # Push all characters of the word onto the stack
    for char in word:
        stack.push(char)
    
    # Pop all characters from the stack and build the reversed word
    reversed_word = ''
    while not stack.is_empty():
        reversed_word += stack.pop()
    
    return reversed_word





# Example usage
print("enter a word")
word = str(input())
reversed_word = rev(word)
print("Original word:", word)
print("R:", reversed_word)
