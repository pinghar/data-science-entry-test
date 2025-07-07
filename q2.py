def find_and_replace(lst, find_val, replace_val):

    Example:
      find_and_replace([1, 2, 3, 2], 2, 5) -> [1, 5, 3, 5]
    """
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    # Use list comprehension to produce a new list with replacements
    return [replace_val if x == find_val else x for x in lst]


# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Scenario 1 result:", result1)
# Expected output: [1, 5, 3, 4, 5, 5]

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Scenario 2 result:", result2)
# Expected output: ["orange", "banana", "orange"]
