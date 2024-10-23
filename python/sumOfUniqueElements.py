def sum_unique_elements(lst):
    # Bug 1: Doesn't handle empty list properly (no default return)
    
    # Bug 2: Using list instead of set, which is inefficient and might miss duplicates
    unique = []
    for i in lst:
        if not i in unique:
            unique.append(i)
    
    # Bug 3: Doesn't handle non-numeric elements
    sum = 0
    for num in unique:
        sum = sum + num
    
    # Bug 4: Name conflict with built-in 'sum' function
    return sum

# Example usage with bugs
test_list = [1, 2, 2, 3, 3, 3, 'a', 4]
print(sum_unique_elements(test_list))  # Will crash when it hits 'a'

# Bug 5: These edge cases aren't handled:
print(sum_unique_elements([]))  # Will run but gives no explicit return for empty list
print(sum_unique_elements([None, 1, 2]))  # Will crash on None
