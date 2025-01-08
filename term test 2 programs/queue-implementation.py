class Full (Exception):
    pass

class Empty(Exception):
    pass

class QueueArray:
    def __init__ (self, capacity = 10):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0
        self.capacity = capacity


    def frontElement(self):
        if self.isEmpty():
            raise Empty("Queue underflow")
        return self.data[self.front]

    
    def isEmpty(self):
        return self.size == 0


    def __len__(self):
        if self.isEmpty():
            raise Empty("Queue uderflow condition")
        return self.data("Queue underflow")


    def enqueue(self, element):
        if self.size == self.capacity:
            raise Full("Queue Overflow condition")
        avail = (self.front + self.size) % self.capacity
        self.data[avail] = element
        self.size += 1


    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow Condition")
            return
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            print(self.data[index], end=' ')
        print()


if __name__ == "__main__":
    q = QueueArray(5)
    q.display()
    q.enqueue(10)
    q.display()
    q.enqueue(20)
    q.display()
    q.enqueue(40)
    q.display()
    print(q.frontElement())    


