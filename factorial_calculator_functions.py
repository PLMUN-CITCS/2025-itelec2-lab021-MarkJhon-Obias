def get_non_negative_integer():
    n = int(input("Enter a none-negative integer: "))
    return n

def calculate_factorial(n):
    """Calculates the factorial of a given number."""
    if n == 0:
        return 1  # Factorial of 0 is 1

    factorial = 1  # Initialize factorial variable
    for i in range(1, n + 1):
        factorial *= i  # Multiply each number in range

    return factorial  # Return the final factorial value


if __name__ == "__main__":
    result1 = get_non_negative_integer()
    final_result1 = calculate_factorial(result1)
    print(f"The factorial of {result1} is: {final_result1}\n")

    result2 = get_non_negative_integer()
    final_result2 = calculate_factorial(result2)
    print(f"The factorial of {result2} is: {final_result2}\n")
