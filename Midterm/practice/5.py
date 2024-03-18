def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False

# Example usage:
input_string = "racecar"
print("Is", input_string, "a palindrome?", is_palindrome_recursive(input_string))
