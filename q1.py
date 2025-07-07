def swap(x, y):
    
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    x, y = y, x
    print("Swapped values:", x, y)
    return x, y

# Scenario 1: "Apple", 10
result1 = swap("Apple", 10)
print("Result:", result1)  # Expected output: -1

# Scenario 2: 9, 17
result2 = swap(9, 17)
print("Result:", result2)  # Expected output: Swapped values: 17 9
                           # Result: (17, 9)
