def fibonacci(n):
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    n (int): The number of Fibonacci numbers to generate. Must be a positive integer.

    Returns:
    list: A list of the first n Fibonacci numbers.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Handle the edge case for n = 1
    if n == 1:
        return [0]

    # Initialize the Fibonacci sequence with the first two values
    fib_sequence = [0, 1]
    
    # Generate Fibonacci numbers starting from the third element
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Allow user input
try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(fibonacci(n))
except ValueError as e:
    print(e)
