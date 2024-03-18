def power_recursive_tail(base, exponent, result=1):
    if exponent == 0:
        return result
    elif exponent < 0:
        return power_recursive_tail(base, exponent + 1, result / base)
    else:
        return power_recursive_tail(base, exponent - 1, result * base)

# Example usage:
base_number = 2
exponent_number = 5
print("The result of", base_number, "raised to the power of", exponent_number, "is:", power_recursive_tail(base_number, exponent_number))
