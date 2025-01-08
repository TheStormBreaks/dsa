class SinglyLinkedList:
    #0
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element):
            self._element = element
            self._next = None
            #self._prev = None

    #class Node:
    #  slots = 'element', 'next'
    #
    #def init (self, element):
    #   self.element = element
    #   self.next = None

    #1 
    def __init__(self):
        self._head = None
        self._size = 0

    #2
    def __len__(self):
        return self._size


    #3
    def is_empty(self):
        return self._size == 0
    
    
    def top(self):
        return self._head


    #4
    def insert_at_start(self, data):
        newest = self._Node(data)
        newest._next=self._head
        self._head=newest
        self._size=self._size+1



    def insert_at_end(self, data):
        newest = self._Node(data)
        if self._head is None:
            self._head = newest
            return
        n = self._head
        while n._next is not None:
            n = n._next
        n._next = newest
        self._size=self._size+1



    def delete_at_start(self):
        if self._head is None:
            print("The list has no element to delete")
            return
        answer=self._head._element
        self._head = self._head._next
        self._size=self._size-1
        return answer
    

    def print_second_last(self):
      # Check if the list has fewer than 2 elements
        if self._head is None or self._head._next is None:
           print("List has less than 2 elements")
           return
    
        # Initialize two pointers
        second_last = None

        
        n = self._head
    
        # Traverse the list
        while n._next is not None:
           second_last = n
           n = n._next
    
        # Print the second last element
        if second_last is not None:
           print("Second last element is:", second_last._element)
 


    # def traverse_list(self):
    #   if self._head is None:
    #      print("List has no element")
    #        return
    #    else:
    #        n = self._head
    #        while n is not None:
    #            print(n._element, " ")
    #            n = n._next


                
               
               
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
    s=SinglyLinkedList()
    s.insert_at_start(11)
    s.insert_at_start(1232)
    s.insert_at_end(696969)
    s.display()
    s.insert_at_end(15)
    s.display()
    s.insert_at_start(10)
    s.display()
    print()
    print("second last is:")
    s.print_second_last()
    s.display()
    print(s.is_empty())
    s.delete_at_start()
    s.display()
    