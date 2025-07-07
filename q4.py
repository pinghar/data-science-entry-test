def string_reverse(s):
    
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    # Pythonic reverse using slicing
    return s[::-1]


# Scenario 1
result1 = string_reverse("Hello World")
print("Reversed:", result1)
# Expected output: Reversed: dlroW olleH

# Scenario 2
result2 = string_reverse("Python")
print("Reversed:", result2)
# Expected output: Reversed: nohty
