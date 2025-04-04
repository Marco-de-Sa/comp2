def binary_search_with_in(arr, target):
    """
    Perform a binary search using the 'in' operator to check halves of the list.

    :param arr: List of elements
    :param target: Element to search for
    :return: Index of the target element if found, otherwise -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is in the left half
        if target in arr[left:mid + 1]:
            right = mid
        # Check if the target is in the right half
        elif target in arr[mid + 1:right + 1]:
            left = mid + 1
        else:
            # Target not found
            return -1

        # If the range narrows to a single element, check it
        if left == right and arr[left] == target:
            return left

    return -1


# Example usage
import random

# Initialize the list
arr = [0, 0, 0, 0, 0, 0, 0]

# Set a random index to 1
random_index = random.randint(0, len(arr) - 1)
arr[random_index] = 1
print(arr)

# Perform binary search for 1
result = binary_search_with_in(arr, 1)

# Output the result
print(f"Binary search result: {result}")