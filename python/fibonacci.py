def fibonacci(n):
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Initialize the Fibonacci sequence
    fib_sequence = []
    
    # Generate Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

try:
    n = 10  # Change this value to generate more or fewer Fibonacci numbers
    print(fibonacci(n))
except ValueError as e:
    print(e)
