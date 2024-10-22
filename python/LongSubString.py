def longest_substring(s):
    """
    Returns the length of the longest substring without repeating characters.
    """
    max_len = 0
    start = 0
    char_index = {}

    for i in range(len(s)):
        # Check if the character was seen before and is within the current substring
        if s[i] in char_index and char_index[s[i]] >= start:
            # Move the start index to the right of the last occurrence of the character
            start = char_index[s[i]] + 1  # Fixed: Should be char_index[s[i]] + 1

        # Update the last index of the character
        char_index[s[i]] = i

        # Correctly calculate the length of the current substring
        current_len = i - start + 1  # Fixed: Should be i - start + 1
        max_len = max(max_len, current_len)

    return max_len

# Test cases
print(longest_substring("abcabcbb"))  # Output: 3 (The substring is "abc")
print(longest_substring("bbbbb"))     # Output: 1 (The substring is "b")
print(longest_substring("pwwkew"))    # Output: 3 (The substring is "wke")
print(longest_substring(""))           # Output: 0 (Empty string case)
print(longest_substring(" "))          # Output: 1 (Single space character)
