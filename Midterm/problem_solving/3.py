def count_duplicates(lst):
    """
    Function to count duplicate elements in a list.

    Args:
    lst (list): Input list of elements.

    Returns:
    int: Count of duplicate elements.
    """
    # Create an empty dictionary to store counts of each element
    element_counts = {}

    # Count occurrences of each element in the list
    for element in lst:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # Count how many elements have counts greater than 1
    duplicate_count = sum(1 for count in element_counts.values() if count > 1)

    return duplicate_count

# Example usage:
my_list = [1, 2, 3, 4, 1, 2, 3, 4, 5]
print(count_duplicates(my_list))  # Output should be 4
