def gcd_recursive(a, b):
    
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

# Example usage:
num1 = 48
num2 = 18
print("The GCD of", num1, "and", num2, "is:", gcd_recursive(num1, num2))
