# Function to check if a number is an Armstrong number
def is_armstrong(num):
    # Convert the number to a string to find the number of digits
    num_str = str(num)
    n = len(num_str)

    # Calculate the sum of each digit raised to the power of n
    result = sum(int(digit) ** n for digit in num_str)

    # Check if the result is equal to the original number
    return result == num

# Main function
if __name__ == "__main__":
    # Take input from the user
    number = int(input("Enter a number: "))

    # Check if the number is an Armstrong number
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
