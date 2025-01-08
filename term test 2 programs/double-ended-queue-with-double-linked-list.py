class DoubleLinkedList:
    class Node:
        __slots__ = 'element', 'prev', 'next'
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def insert_in_between(self, e, predecessor, successor):
        newest = self.Node(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest
    
    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element
    

class DoubleEndedQueuewithDoubleLinkedList(DoubleLinkedList):
    def first(self):
        if self.is_empty():
            raise Exception("Dequeue is empty")
        return self.trailer.prev.element
    
    def insert_first(self, e):
        self.insert_in_between(e, self.header, self.header.next)

    def insert_last(self, e):
        self.insert_in_between(e, self.trailer.prev, self.trailer)

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.delete_node(self.header.next)
    
    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.delete_node(self.trailer.prev)
    
    def print_deque(self):
        if self.is_empty():
            print("Empty")
            return
        current = self.header.next
        elements = []
        while current!= self.trailer:
            elements.append(current.element)
            current = current.next
        print("Deque: ", elements)

# deque.insert_first(10) 
# [10]
# deque.insert_first(5) 
# [5, 10]
# deque.insert_last(90)
# [5, 10, 90]
# deque.insert_last(15) 
# [5, 10, 90, 15]
# deque.print_deque() 
# [5, 10, 90, 15]
# deque.delete_last() 
# [5, 10, 90]
# deque.delete_first()
# [10, 90]
# deque.print_deque() 
# [10, 90]
# deque.delete_last()
# deque.delete_last()
# []
# deque.is_empty()
# True


deque = DoubleEndedQueuewithDoubleLinkedList()  
deque.insert_first(10) 
deque.print_deque()
deque.insert_first(5)
deque.print_deque() 
deque.insert_last(90)
deque.print_deque()
deque.insert_last(15) 
deque.print_deque()
deque.print_deque() 
deque.print_deque()
deque.delete_last() 
deque.print_deque()
deque.delete_first()
deque.print_deque() 
deque.delete_last()
deque.print_deque()
deque.delete_last()
deque.print_deque()
deque.is_empty()
deque.print_deque()