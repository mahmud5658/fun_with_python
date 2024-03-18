def sum_of_digits_recursive(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits_recursive(n // 10)

# Example usage:
number = 12345
print("The sum of digits of", number, "is:", sum_of_digits_recursive(number))
