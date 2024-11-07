# Function to perform selection sort
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Driver code to test the selection sort
arr = [64, 25, 12, 22, 11]  # Example array
print("Original array:", arr)

selection_sort(arr)  # Perform selection sort

print("Sorted array:", arr)
