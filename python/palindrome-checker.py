def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.

    A palindrome reads the same forwards and backwards, ignoring
    case and non-alphanumeric characters.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

def main():
    # Get user input
    user_input = input("Enter a string to check if it's a palindrome: ")

    # Check and display the result
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
