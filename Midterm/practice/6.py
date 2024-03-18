def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5
result_index = binary_search_recursive(sorted_list, target_element, 0, len(sorted_list) - 1)
if result_index != -1:
    print("Element", target_element, "found at index", result_index)
else:
    print("Element", target_element, "not found in the list.")
