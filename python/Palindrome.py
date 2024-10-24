def is_palindrome(word: str) -> bool:
    """Returns True if the word is a palindrome, False otherwise."""
    # Normalize the word by converting it to lowercase and removing non-alphanumeric characters
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

# Example test cases
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(is_palindrome("Racecar"))                           # Output: True
print(is_palindrome("Hello"))                             # Output: False
