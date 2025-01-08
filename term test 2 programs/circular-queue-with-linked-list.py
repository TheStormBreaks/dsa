class CircularQueue: 
    class _Node: 
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None): 
            self._element = element 
            self._next = next 
      
    def __init__(self):
        self._tail = None                  
        self._size = 0
 
    def __len__(self): 
        return self._size 
 
    def is_empty(self): 
        return self._size == 0 
 
    def first(self): 
        if self.is_empty(): 
            raise Empty('Queue is empty') 
        #head =  self._tail._next
        return self._tail._next
 
    def dequeue(self): 
        if self.is_empty():
            raise Empty('Queue is empty') 
        oldhead = self._tail._next 
        if self._size == 1:  
            self._tail = None  
        else: 
            self._tail._next = oldhead._next 
        self._size -= 1 
        return oldhead._element 

    def enqueue(self, element): 
        newest = self._Node(element)  
        if self.is_empty(): 
            newest._next = newest 
        else: 
            newest._next = self._tail._next 
            self._tail._next = newest
        self._tail = newest 
        self._size += 1

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self._tail._next 
        elements = [] 
        for _ in range(self._size):  
            elements.append(current._element)
            current = current._next
        print(elements)


# Example Usage
cq = CircularQueue()
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(70)
cq.display() 
cq.dequeue()
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(40)
cq.display()
cq.enqueue(50)
cq.display()
cq.enqueue(100)
cq.display()
cq.dequeue()
cq.display