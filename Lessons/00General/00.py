def quick_sort(arr):
    # Base case: if the list contains 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Select a pivot element (here, we choose the first element)
    pivot = arr[0]

    # Partitioning step: divide the list into two sublists
    # Elements smaller than the pivot go to the left, and larger ones go to the right
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # Recursively sort the sublists (excluding the pivot)
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # Combine the sorted sublists and the pivot to get the final sorted list
    return sorted_left + [pivot] + sorted_right


# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print("Sorted numbers:", sorted_numbers)
