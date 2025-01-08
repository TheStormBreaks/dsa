import time

# Step 1: Quick Sort function definition
def quick_sort(arr):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Step 2: Choose a pivot (last element for simplicity)
    pivot = arr[-1]
    
    # Step 3: Partition the array into two subarrays
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Step 4: Recursively sort the subarrays and combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# Step 3: Test the quick_sort function with an example
if __name__ == "__main__":
    unsorted_array = [12, 7, 5, 9, 3, 11, 1, 4, 10, 8]

    # Measure the time taken to sort the array
    start_time = time.time()
    sorted_array = quick_sort(unsorted_array)
    end_time = time.time()

    print("Unsorted Array: ", unsorted_array)
    print("Sorted Array: ", sorted_array)
    print(f"Time taken to sort the array: {end_time - start_time:.6f} seconds")
