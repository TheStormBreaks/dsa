class EvenNumbersArray:
    def __init__(self):
        self.even_numbers = []

    def generate_even_numbers(self, x, y):
        # Ensure that x is less than y
        if x > y:
            print("Invalid range: x should be less than y.")
            return
        # Add even numbers to the array
        for num in range(x, y + 1):
            if num % 2 == 0:
                self.even_numbers.append(num)  # O(1) per append operation

    def print_even_numbers(self):
        print("Even Numbers:", self.even_numbers)  # O(n)

    def get_length(self):
        return len(self.even_numbers)  # O(1)

# Create the EvenNumbersArray instance
x = 19  # Your age
y = 51  # Father's age
even_numbers_array = EvenNumbersArray()

# Generate even numbers between x and y
even_numbers_array.generate_even_numbers(x, y)

# Print the even numbers and the length of the array
even_numbers_array.print_even_numbers()
print("Length of the list:", even_numbers_array.get_length())

