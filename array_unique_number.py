list1=[9, 43, 12, 30, 21, 36, 18, 13, 26, 48, 34, 37, 16, 3, 4, 45, 14, 41, 11,11, 17]
def unique(list1):
    # Use a set to keep track of seen numbers
    seen = set()
    for num in list1:
        if num in seen:
            return num  # Return the first non-unique number
        seen.add(num)
    return None  # Return None if all numbers are unique

# Call the function and print the result
result = unique(list1)
print("First non-unique number:", result)