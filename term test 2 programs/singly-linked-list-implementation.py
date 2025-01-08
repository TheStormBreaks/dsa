class SinglyLinkedList:
    class _Node:
        __slots__ = '_element' , '_next'

        def __init__(self, element):
            self._element = element
            self._next = None

    
    def __init__(self):
        self._head = None
        self._size = 0


    #length of linked list
    def __len__(self):
        return self._size
    

    #size of linked list
    def is_empty(self):
        return self._size == 0


    def first(self):
        return self._head
    

    #inset at start of the linked list
    def insert_at_start(self, data):
        newest = self._Node(data)
        newest._next = self._head
        self._head = newest
        self._size = self._size + 1


   #insert at the end of the linked list
   #we have to traverse till the end of the list
   #to find the tail node and point it to newest node
    def insert_at_end(self, data):
        newest = self._Node (data)
        if self._head is None:
            self._head = newest
            return
        n = self._head
        while n._next is not None:
            n = n._next
        n._next = newest
        self._size = self._size + 1

    
    def delete_at_start(self):
        if self._head is None:
            print("The lsit has no elements to delete")
            return
        answer = self._head._element
        self._head = self._head._next
        self._size = self._size + 1


               
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
    s = SinglyLinkedList()
    s.insert_at_start(11)
    s.insert_at_start(1232)
    s.insert_at_end(696969)
    s.display()
    s.insert_at_end(15)
    s.display()
    s.insert_at_start(10)
    s.display()
    print("Is the stack empty?", s.is_empty())
    s.delete_at_start()
    s.display()


