"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""
def check_integer():
    """
    Prompts for an integer and uses bitwise operations to check its properties.
    """
    try:
        num = int(input("Enter an integer: "))

        if num & 1 == 0:
            print(f"The number {num} is even.")
        else:
            print(f"The number {num} is odd.")

        if num > 0 and (num & (num - 1)) == 0:
            print(f"The number {num} is a power of two.")
        else:
            print(f"The number {num} is not a power of two.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    check_integer()
