def find_first_negative(lst):
    
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"


# Scenario 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("First negative:", result1)
# Expected output: First negative: -1

# Scenario 2
result2 = find_first_negative([2, 10, 7, 0])
print("First negative:", result2)
# Expected output: First negative: No negatives
