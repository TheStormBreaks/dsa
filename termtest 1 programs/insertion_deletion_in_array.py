class Array:
    def __init__(self, capacity = 10):
        self.data = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def InsertAtIndex(self, index, ele):
        if self.size == self.capacity:
            print("Array Overflow.")
            return
        if index > self.size:
            index = self.size
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = ele
        self.size = self.size + 1

    def InsertAtLast(self, ele):
        if self.size == self.capacity:
            print("Array Overflow")
            return
        self.data[self.size] = ele
        self.size += 1

    def InsertAtStart(self, ele):
        self.InsertAtIndex(0, ele)

    def DeleteAtIndex(self, index):
        if self.size == 0:
            print("Array Underflow")
            return
        deleteValue = self.data[index]
        for i in range (index, self.size - 1):
            self.data[i] = self.data[i+1]
        self.data[self.size - 1] = None
        self.size -= 1
        return deleteValue
    
    def DeleteAtStart(self):
        return self.DeleteAtIndex(0)
    
    def DeleteAtLast(self):
        if self.size == 0:
            print("Array Underflow")
            return
        deleteValue = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return deleteValue
    
    def len(self):
        return self.size
    
    def TraverseArray(self):
        for i in range(self.size):
            print(self.data[i], end = " ")


if __name__ == "__main__":
    a1 = Array()
    a2 = Array(15)
    print(a1.data)

    a1.InsertAtStart(15)
    a1.InsertAtStart(14)
    a1.InsertAtIndex(1, 16)
    a1.InsertAtLast(20)
    a1.InsertAtIndex(9, 16)
    print(a1.data)

        