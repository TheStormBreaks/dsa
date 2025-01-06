class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)  # O(1)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # O(1)
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # O(1)
        return None
    
    def is_empty(self):
        return len(self.items) == 0  # O(1)
    
    def size(self):
        return len(self.items)  # O(1)

def isit_balanced(string):
    stack = Stack()
    matching_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return False
    
    return stack.is_empty()

print(isit_balanced("{[()]}"))  # True
print(isit_balanced("{[(])}"))  # False
print(isit_balanced("{{[[(())]]}}"))  # True
print(isit_balanced(""))  # True
