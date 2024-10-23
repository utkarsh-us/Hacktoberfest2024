def sum_unique_elements(lst):
    if not lst:
        return 0
    
    unique_elements = set()
    total_sum = 0
    for i in lst:
        if isinstance(i, (int, float)) and i not in unique_elements:
            unique_elements.add(i)
            total_sum += i
    
    return total_sum

test_list = [1, 2, 2, 3, 3, 3, 'a', 4]
print(sum_unique_elements(test_list))

print(sum_unique_elements([]))
print(sum_unique_elements([None, 1, 2]))
