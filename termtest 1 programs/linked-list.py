class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None 
        self.size = 0
        
    
    def insertAtHead(self, ele):
        newNode = Node(ele, self.head)
        if newNode == None:
            print("Couldn't creat a new node!!!")
            return
        #newNode.data = ele 
        #newNode.next = self.head
        self.head = newNode
        self.size += 1 
        
    def deleteAtHead(self):
        if self.head == None:
            raise Exception("Linked underflow!!!")
            
        deletedValue = self.head.data 
        self.head = self.head.next
        self.size -= 1 
        return deletedValue
     
    def insertAtTail(self, ele):
        newNode = Node(ele, None)
        if newNode == None:
            print("Couldn't create a new node!!!")
            return
        
        if self.size == 0:
            self.head = newNode 
            self.size += 1 
            return 
        currentNode = self.head 
        tailNode = None
        while(currentNode):
            if currentNode.next == None:
                tailNode = currentNode 
                break 
            currentNode = currentNode.next 
        
        tailNode.next = newNode
        self.size += 1 
        
    def deleteAtTail(self):
        if self.size == 0:
            print("LinkedList empty!!!!!")
            return 
        previousNode = self.head 
        currentNode = self.head 
        while(currentNode):
            if currentNode.next == None:
                break 
            previousNode = currentNode 
            currentNode = currentNode.next 
        deletedValue = currentNode.data 
        previousNode.next = None 
        self.size -= 1 
        if self.size == 0:
            self.head = None 
        return deletedValue
    def insertAfter(self, ele, previousNodeValue):
        newNode = Node(ele)
        if newNode == None:
            print("couldn't create new node ")
            return 
        previousNode = self.head 
        
        while(previousNode):
            if previousNode.data == previousNodeValue:
                break 
            previousNode = previousNode .next 
        newNode.next = previousNode.next 
        previousNode.next = newNode 
        self.size = self.size + 1 
        
    def __len__(self): 
        return self.size
            
            
   
    def traverseLinkedList(self):   
        currentNode = self.head
        while(currentNode):
            print(currentNode.data, end =" ")
            currentNode = currentNode.next 
            
    
     

if __name__ == "__main__":
    l1 = LinkedList()
    l1.insertAtTail(50)
    l1.insertAtHead(10)
    l1.insertAtHead(20)
    l1.insertAtTail(40)
    l1.insertAfter(70, 20)
    

    print("deleted value: ",l1.deleteAtTail())
    print("Len: ", len(l1))

    l1.traverseLinkedList()
    
    