def update_dictionary(dct, key, value):

    if not isinstance(dct, dict):
        raise TypeError("dct must be a dictionary")
    
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    dct[key] = value
    return dct

# Scenario 1: Add a new key
result1 = update_dictionary({}, "name", "Alice")
print("Result 1:", result1)
# Output:
# Result 1: {'name': 'Alice'}

# Scenario 2: Update an existing key
result2 = update_dictionary({"age": 25}, "age", 26)
# Output:
# Original value for 'age': 25
print("Result 2:", result2)
# Result 2: {'age': 26}
