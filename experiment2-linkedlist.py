class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_values(self, data_list):
        for data in data_list:
            self.append(data)
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
    
    def insert_after_value(self, data_after, data_to_insert):
        if not self.head:
            print(f"List is empty. Cannot insert {data_to_insert} after {data_after}.")
            return
        
        current = self.head
        while True:
            if current.data == data_after:
                new_node = Node(data_to_insert)
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
            if current == self.head:  
                break
        print(f"Value {data_after} not found in the list.")
    
    def remove_by_value(self, data):
        if not self.head:
            print(f"List is empty. Cannot remove {data}.")
            return
        
        current = self.head
        while True:
            if current.data == data:
                if current.next == current:  
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:  
                        self.head = current.next
                return
            current = current.next
            if current == self.head: 
                break
        print(f"Value {data} not found in the list.")
    
    def print_forward(self):
        if not self.head:
            print("List is empty.")
            return
        
        current = self.head
        result = []
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(result))
    
    def print_backward(self):
        if not self.head:
            print("List is empty.")
            return
        
        current = self.head.prev 
        result = []
        while True:
            result.append(current.data)
            current = current.prev
            if current == self.head.prev:
                break
        print(" <- ".join(result))


# Testing the Circular Doubly Linked List
LL = CircularDoublyLinkedList()
LL.insert_values(["Red", "Yellow", "Purple", "Orange"])
LL.print_forward()
LL.insert_after_value("Yellow", "Blue") 
LL.print_forward()
LL.remove_by_value("Orange")  
LL.print_forward()
LL.remove_by_value("Green")  
LL.print_forward()
LL.remove_by_value("Red")
LL.remove_by_value("Yellow")
LL.remove_by_value("Blue")
LL.remove_by_value("Purple")
LL.print_forward()
LL.print_forward()
LL.print_backward()
