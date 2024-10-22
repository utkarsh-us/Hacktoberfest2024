# hacktoberfest_challenge.py
# A simple Python script that contains a few bugs. Feel free to fix them and improve the code!

def is_prime(number):
    """Returns True if the number is prime, else False."""
    if number <= 1:
        return True  # Bug: 1 is not prime!
    for i in range(2, number):  # Bug: Should be range(2, int(number**0.5) + 1)
        if number % i == 0:
            return False
    return True

def sum_of_primes(limit):
    """Returns the sum of all prime numbers up to the given limit."""
    total = 0
    for num in range(1, limit):  # Bug: Should start from 2, since 1 is not prime
        if is_prime(num):
            total += num
    return total

def main():
    """Main function to demonstrate the prime number functions."""
    number = int(input("Enter a number: "))  # Bug: No validation for non-integer input
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    
    limit = int(input("Enter the upper limit for sum of primes: "))  # Bug: Same input validation issue
    print(f"The sum of primes up to {limit} is: {sum_of_primes(limit)}")

if __name__ == "__main__":
    main()
