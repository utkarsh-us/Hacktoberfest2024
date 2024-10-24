def sum_unique_elements(lst):
    """
    Returns the sum of unique numeric elements in the list.
    Non-numeric elements are ignored.
    """
    if not lst:
        return 0  # Return 0 for an empty list
    
    unique_elements = set()  # Track unique numbers
    total_sum = 0  # Sum of unique numbers
    
    for item in lst:
        # Check if item is numeric (int or float) and not already in unique_elements
        if isinstance(item, (int, float)) and item not in unique_elements:
            unique_elements.add(item)
            total_sum += item
    
    return total_sum  # Return the total sum

# Test cases
test_list = [1, 2, 2, 3, 3, 3, 'a', 4]
print(sum_unique_elements(test_list))  # Output: 10
print(sum_unique_elements([]))  # Output: 0
print(sum_unique_elements([None, 1, 2]))  # Output: 3
print(sum_unique_elements([5, 5.0, 10, '10']))  # Output: 15 (5 and 5.0 are considered the same)
