"""
Challenge: Convert Decimal to Binary

Write a function that accepts a decimal number and returns the equivalent binary number.

Rules:
- The decimal number will always be less than 1024.
- The binary number returned should be a string representation (e.g., '1010').
- Do NOT use Python’s built-in bin() function.
"""

def decimal_to_binary(decimal_number):
    """
    Convert a decimal number into its binary representation.

    Parameters:
        decimal_number (int): The decimal number to convert (less than 1024).

    Returns:
        str: The binary representation of the number.
    """
    # TODO: Write your code here
    pass


if __name__ == "__main__":
    example_decimal = 10
    result = decimal_to_binary(example_decimal)
    print(f"The binary of {example_decimal} is {result}")
