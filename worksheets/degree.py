"""
Challenge: Convert Radians to Degrees

Write a function that accepts one numeric parameter — the measure of an angle in radians.
The function should convert the radians into degrees and return that value.

Rules:
- Do NOT use any built-in Python function for this (e.g., math.degrees()).
- You MAY import the value of Pi from the math module.
- Formula hint: degrees = radians * (180 / Pi)
"""

# Import Pi from the math module
from math import pi


def radians_to_degrees(radians_value):
    """
    Convert an angle from radians to degrees.

    Parameters:
        radians_value (float): The angle in radians.

    Returns:
        float: The angle converted to degrees.
    """
    # TODO: Write your code here
    # Remember: degrees = radians_value * (180 / pi)
    pass


# Example usage (you can modify or comment this out during testing)
if __name__ == "__main__":
    example_radians = 3.14159  # roughly pi radians
    result = radians_to_degrees(example_radians)
    print(f"{example_radians} radians is equal to {result} degrees")
