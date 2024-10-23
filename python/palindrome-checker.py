def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Get user input
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
