# Initialize the array
snaj = [10, 20, 30, 40, 50]

#print(array[0])

# 1. Access element at a specific index (n)
# Returns the element at index `n` if within range; otherwise, it gives an error message
def get_element(array, n):
    if n < len(array):
        return array[n]
    else:
        return "Index out of range"

# 2. Access element at index 0
# Returns the first element (element at index 0)
def get_first_element(array):
    return array[0] if array else "Array is empty"

# 3. Print the array
# Prints the entire array
def print_array(array):
    print("Array:", array)

# 4. Insert new element
# Inserts a new element. If `index` is specified, 
# it inserts there; otherwise, it appends to the end
def insert_element(array, element, index=None):
    if index is None:  # Insert at the end if no index is specified
        array.append(element)
    elif 0 <= index <= len(array):  # Insert at specified index
        array.insert(index, element)
    else:
        print("Index out of range")

# 5. Delete element at any index
# Deletes the element at the specified `index` if it’s within range
def delete_element(array, index):
    if 0 <= index < len(array):
        array.pop(index)
    else:
        print("Index out of range")

# Demonstrating the functions
# Initial array
print("Initial array:")
print_array(snaj)

# Access element at index 2
print("Element at index 2:", get_element(snaj, 2))


get_element()

# Access element at index 0
print("Element at index 0:", get_first_element(snaj))

# Insert new element 60 at the end
insert_element(snaj, 60)
print("Array after inserting 60 at the end:")
print_array(snaj)

# Insert new element 25 at index 2
insert_element(snaj, 25, 2)
print("Array after inserting 25 at index 2:")
print_array(snaj)

# Delete element at index 3
delete_element(snaj, 3)
print("Array after deleting element at index 3:")
print_array(snaj)
