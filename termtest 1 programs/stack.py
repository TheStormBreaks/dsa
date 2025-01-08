class Stack:
    def __init__ (self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)

    def pop (self):
        if self.is_empty():
            return "Empty Stack"
        return self.stack.pop()
    
    def size (self):
        if self.is_empty():
            return "Empty Stack"
        return len(self.stack)
    
    def display(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            print("Stack: ", self.stack)

    def peek(self):
        if self.is_empty():
            return "Empty Stack"
        return self.stack[-1]
    
if __name__ == "__main__":
    s = Stack()

    print("Enter the first number: ")
    num1 = int(input())
    print("Enter the second number: ")
    num2 = int(input())
    print("Enter the third number")
    num3 = int(input())

    s.push(num1)
    s.push(num2)
    s.push(num3)
    print("After pushing in", num1, ",", num2, "and", num3, ":")
    s.display()

    print("\nPopping an element:", s.pop())
    print("After popping, the stack is: ")
    s.display()
    s.peek()

    print("Size of the stack: ", s.size())

    #here we empty the stack
    s.pop()
    s.pop()
    print("after popping all the elements: ")
    s.display()

