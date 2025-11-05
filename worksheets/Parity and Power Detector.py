"""
This script prompts the user to enter a number, then determines if the number is even or odd,
and checks whether it is a power of 2. Usage: Run the script and input an integer when prompted.
"""

num = int(input("Enter a number: "))


print(f"{num} is {'even' if num % 2 == 0 else 'odd'}")


if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a power of 2")
else:
    print(f"{num} is not a power of 2")