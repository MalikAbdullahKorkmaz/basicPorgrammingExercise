def sum_of_digits(n):
    """
    Calculates the sum of digits in a given integer.

    Parameters:
    n (int): The integer whose sum of digits is to be calculated.

    Returns:
    int: The sum of digits in the given integer.
    """
    return sum(int(digit) for digit in str(n))

# Test the function
num = 12345
print("Sum of digits in", num, "is:", sum_of_digits(num))