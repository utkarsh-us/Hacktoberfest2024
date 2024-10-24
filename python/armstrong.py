def is_armstrong(number):
    """
    Check if the given number is an Armstrong number.

    An Armstrong number for an n-digit number is a number that equals the sum
    of its digits raised to the power of n.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is an Armstrong number, False otherwise.
    """
    # Ensure the number is non-negative
    if number < 0:
        return False

    # Get the number of digits
    n = len(str(number))
    
    # Calculate the sum of digits each raised to the power of n
    result = sum(int(digit) ** n for digit in str(number))
    
    return result == number

def main():
    """
    Main function to take user input and check if the number is an Armstrong number.
    """
    try:
        # Take input from the user
        number = int(input("Enter a positive integer: "))

        # Check if the number is an Armstrong number
        if is_armstrong(number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")
    
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
