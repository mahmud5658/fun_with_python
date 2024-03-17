def count_duplicates(lst):

    # Create an empty dictionary to store counts of each element
    element_counts = {}

    # Count occurrences of each element in the list
    for element in lst:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # Filter elements with counts greater than 1
    duplicate_elements = {}
    for key, value in element_counts.items():
       if value > 1:
         duplicate_elements[key] = value

    return duplicate_elements

# Sample Input 1
lst = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana']
print("Count of duplicate elements:", count_duplicates(lst))
