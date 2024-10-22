def longest_substring(s):
    """
    Returns the length of the longest substring without repeating characters.
    """
    max_len = 0
    start = 0
    char_index = {}

    for i in range(len(s)):
        # Bug 1: Incorrect condition to check if the character was seen before.
        if s[i] in char_index and char_index[s[i]] >= start:
            start = i  # Bug 2: Should be char_index[s[i]] + 1, not i

        # Update the last index of the character
        char_index[s[i]] = i

        # Bug 3: Incorrect length calculation, should be i - start + 1
        current_len = i - start
        max_len = max(max_len, current_len)

    return max_len
