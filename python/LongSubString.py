def longest_substring_without_repeating_characters(s):
    """
    Returns the length of the longest substring without repeating characters.

    Parameters:
    s (str): The input string to search.

    Returns:
    int: The length of the longest substring without repeating characters.
    """
    # Edge case: If the string is empty, return 0
    if not s:
        return 0
    
    max_length = 0
    start = 0
    last_seen = {}

    # Iterate over each character in the string
    for i, char in enumerate(s):
        # If the character has been seen and its index is within the current window
        if char in last_seen and last_seen[char] >= start:
            # Update the start of the window to be after the last occurrence of the character
            start = last_seen[char] + 1

        # Update the last seen index of the character
        last_seen[char] = i

        # Calculate the length of the current substring
        current_length = i - start + 1
        max_length = max(max_length, current_length)

    return max_length

# Test cases
print(longest_substring_without_repeating_characters("abcabcbb"))  # Output: 3 ("abc")
print(longest_substring_without_repeating_characters("bbbbb"))     # Output: 1 ("b")
print(longest_substring_without_repeating_characters("pwwkew"))    # Output: 3 ("wke")
print(longest_substring_without_repeating_characters(""))          # Output: 0 (empty string)
print(longest_substring_without_repeating_characters(" "))         # Output: 1 (" ")