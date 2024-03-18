def reverse_string_recursive(s):

    if len(s) <= 1: 
        return s
    else:
        return s[-1] + reverse_string_recursive(s[1:-1]) + s[0]

# Example usage:
input_string = "hello"
reversed_string = reverse_string_recursive(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
