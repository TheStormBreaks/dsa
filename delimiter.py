class Empty(Exception):
    pass

class ArrayStack:
#LIFO Stack implementation using a Python list as underlying storage

    def __init__(self):
    #Create an empty stack
        self.data =[] # nonpublic list instance

    def __len__(self):
    #Return the number of elements in the stack
        return len(self.data)

    def is_empty(self):
    #Return True if the stack is empty
        return len(self.data) == 0

    def push(self,e):
    #Add element e to the top of the stack
        self. data.append(e) # new item stored at end of list

    def top(self):
    #Return (but do not remove) the element at the top of the stack
        if self.is_empty():
            raise Empty("Stack is empty")
        return self. data[-1] # the last item in the list

    def pop(self):
    #Remove and return the element from the top of the stack (i.e., LIFO)
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data.pop() # remove last item from list
    

# [ ( { } ) ]
def is_matched(expr):
 #Return True if all delimiters are properly match; False otherwise.
    lefty = '( { [' # opening delimiters   ( - [0]   { - [1]  [ - [2]
    righty = ') } ]' # respective closing delims   ) - [0]   } - [1]  ] - [2]
    
    S = ArrayStack( )

    for c in expr:
        if c in lefty:
            S.push(c) # push left delimiter on stack
        elif c in righty:
            if S.is_empty( ):
                return False # nothing to match with. so its not a valid delimiter
            if righty.index(c) != lefty.index(S.pop( )):
                return False # mismatched
    return S.is_empty( )

print(is_matched('[({})]'))
