class Deque:
    def __init__(self, max_size=6):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == -1

    def insert_front(self, value):
        if self.is_full():
            print("Overflow: Cannot insert, deque is full.")
            return

        if self.is_empty():  # First element
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.max_size) % self.max_size
        
        self.queue[self.front] = value

    def delete_rear(self):
        if self.is_empty():
            print("Underflow: Cannot delete, deque is empty.")
            return

        value = self.queue[self.rear]
        self.queue[self.rear] = None  # Optional: Clear the slot

        if self.front == self.rear:  # Last element
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.max_size) % self.max_size

        return value

    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return

        print("Deque contents:", end=" ")
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.max_size
        print()

# Example usage
deque = Deque()

deque.insert_front(10)
deque.insert_front(20)
deque.insert_front(30)
deque.insert_front(40)
deque.insert_front(50)
deque.insert_front(60)

deque.display()

deque.insert_front(70)

deque.display()

deque.delete_rear()
deque.delete_rear()

deque.display()

deque.delete_rear()
deque.delete_rear()
deque.delete_rear()
deque.delete_rear()  # Deleting until empty

deque.delete_rear()
