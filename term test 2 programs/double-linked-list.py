class DoublyLinkedBase:
    class Node:
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self.Node(None)  
        self.tailer = self.Node(None) 
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
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
    
    def display(self):
        current = dll.header.next
        while current != dll.tailer:
            print(current.element)
            current = current.next
        print("list end")
        


# Example Usage
dll = DoublyLinkedBase()

a = dll.insert_between(10, dll.header, dll.tailer)  
dll.display()
b = dll.insert_between(20, a, dll.tailer)    
dll.display()
c = dll.insert_between(15, a, b) 
dll.display()
d = dll.insert_between(69, dll.header, 10)
dll.display()
dll.delete_node(b)  
dll.display()



