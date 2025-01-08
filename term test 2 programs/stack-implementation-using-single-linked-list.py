#stack using single linked list
#S.pop() --> l.delete_at_start
#S.push() --> l.insert_at_start
#S.len() --> l.len()
#S.is_empty() --> l.is_empty()
#S.peek() --> l.first()


class StackWithSinglyLinkedList:
    class _Node:
        __slots__ = '_element' , '_next'

        def __init__(self, element):
            self._element = element
            self._next = None

    def __init__(self):
        self._head = None
        self._size = 0



    #S.pop() --> l.delete_at_start
    def pop(self):
        if self._head is None:
            print("The lsit has no elements to delete")
            return
        answer = self._head._element
        self._head = self._head._next
        self._size = self._size + 1


    #S.push() --> l.insert_at_start
    def push(self, data):
        newest = self._Node(data)
        newest._next = self._head
        self._head = newest
        self._size = self._size + 1


    #S.len() --> l.len()
    def __len__(self):
        return self._size
    
    
    #S.is_empty() --> l.is_empty()
    def is_empty(self):
        return self._size == 0
    
    #S.peek() --> l.first()
    def peek(self):
        return self._head
    
    #traverse and print the stack elements           
    def display(self):
        if self.is_empty():
            print("List is empty")
        else:
            n = self._head
            print("List elements:", end=" ")
            while n:
                print(n._element, end=" ",)
                n = n._next
            print()  # Newline after printing all elements

    


if __name__ == "__main__":
    s = StackWithSinglyLinkedList()
    s.push(11)
    s.push(1232)
    s.push(696969)
    s.display()
    s.push(15)
    s.display()
    s.push(10)
    s.display()
    print("Is the stack empty?", s.is_empty())
    s.pop()
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()
