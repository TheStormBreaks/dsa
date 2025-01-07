class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def size(self):
        if self.is_empty():
            return "Stack is empty"
        return len(self.stack)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stack)






if __name__ == "__main__":
    s = Stack()


    print("Enther the first number")
    num1 = int(input())
    print("Enter the second number")
    num2 = int(input())
    print("Enter the third number")
    num3 = int(input())

    s.push(num1)
    s.push(num2)
    s.push(num3)
    print("After pushing in", num1, ",", num2, "and", num3, ":")
    s.display()

    print("\nPopping an element:", s.myre())
    print("After popping, the stack is: ")
    s.display()

    print("Size of the stack: ", s.size())

    #here we empty the stack
    s.myre()
    s.myre()
    print("after popping all the elements: ")
    s.display()

    print("Now, popping an empty stack: ")
    s.myre()
 