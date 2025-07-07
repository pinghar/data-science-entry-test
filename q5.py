def check_divisibility(num, divisor):
    
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric")
    # Optional: handle division by zero
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    # Use modulo operator: divisible if remainder is zero
    return num % divisor == 0

# Scenario 1: 10 divided by 2
result1 = check_divisibility(10, 2)
print("10 divisible by 2?", result1)
# Expected output: True

# Scenario 2: 7 divided by 3
result2 = check_divisibility(7, 3)
print("7 divisible by 3?", result2)
# Expected output: False
