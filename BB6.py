def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if target is at mid
        if arr[mid] == target:
            return mid
        # If target is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        # If target is larger, ignore left half
        else:
            low = mid + 1

    # Target not found
    return -1


# Example usage
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in list")
