def count_occurrences_recursive(arr, target):
    if not arr:
        return 0
    if arr[0] == target:
        return 1 + count_occurrences_recursive(arr[1:], target)
    else:
        return count_occurrences_recursive(arr[1:], target)

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2]
target_element = 2
occurrences = count_occurrences_recursive(my_list, target_element)
print("The element", target_element, "occurs", occurrences, "times in the list.")
