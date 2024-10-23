def sum_unique_elements(lst):
    """
    Returns the sum of unique numeric elements in the list.
    Non-numeric elements are ignored.
    """
    if not lst:
        return 0 # Return 0 for empty list
    
    unique_elements = set() # Track unique numbers
    total_sum = 0 # Sum of unique numbers
    for i in lst:
        if isinstance(i, (int, float)) and i not in unique_elements:
            unique_elements.add(i)
            total_sum += i
    
    return total_sum # Return the total sum

test_list = [1, 2, 2, 3, 3, 3, 'a', 4]
print(sum_unique_elements(test_list)) # Output: 10

print(sum_unique_elements([])) # Output: 0
print(sum_unique_elements([None, 1, 2])) # Output: 3