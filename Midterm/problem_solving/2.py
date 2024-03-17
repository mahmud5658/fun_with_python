def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

# Example usage:
number = int(input("Enter a number to find its prime factors: "))
print("Prime factors of", number, "are:", prime_factors(number))
