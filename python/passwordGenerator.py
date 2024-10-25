import random
import string

def generate_strong_password(length=12):
    # Ensure minimum length for strong password criteria
    if length < 8:
        print("Password length should be at least 8 characters for a strong password.")
        return None
    
    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with a random mix
    all_characters = upper + lower + digits + special_chars
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle to prevent predictable character positions
    random.shuffle(password)
    
    return ''.join(password)

# User input for password length
length = int(input("Enter desired password length (minimum 8): "))
password = generate_strong_password(length)
if password:
    print("Generated Strong Password:", password)
