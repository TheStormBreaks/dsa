import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    # Convert a list into a Max Heap
    def build_heap(self, elements):
        self.heap = [-el for el in elements]  # Negate to use min-heap as max-heap
        heapq.heapify(self.heap)

    # Insert a new element
    def insert(self, value):
        heapq.heappush(self.heap, -value)

    # Find the maximum element
    def find_max(self):
        return -self.heap[0] if self.heap else None

    # Delete the maximum element (root)
    def delete_max(self):
        return -heapq.heappop(self.heap) if self.heap else None

    # Print the heap
    def print_heap(self):
        print([-el for el in self.heap])

# Example Usage
if __name__ == "__main__":
    elements = [10, 12, 14, 16, 18, 20]
    heap = MaxHeap()
    heap.build_heap(elements)

    print("Initial Max Heap:")
    heap.print_heap()

    # 1. Insert a new element (sum of digits of roll number)
    roll_number = 412012 # Replace with your roll number
    sum_of_digits = sum(int(digit) for digit in str(roll_number))
    print(f"\nInserting element (sum of digits of roll number): {sum_of_digits}")
    heap.insert(sum_of_digits)
    print("Heap after insertion:")
    heap.print_heap()

    # 2. Find the maximum element
    max_element = heap.find_max()
    print(f"\nMaximum element in the Max Heap: {max_element}")

    # 3. Delete the root element (maximum element) twice
    print("\nDeleting the root element (maximum) twice:")
    deleted_1 = heap.delete_max()
    print(f"Deleted element: {deleted_1}")
    heap.print_heap()
    deleted_2 = heap.delete_max()
    print(f"Deleted element: {deleted_2}")
    heap.print_heap()
