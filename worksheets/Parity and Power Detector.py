"""
Input an integer.

Print:
Whether it's even or odd using num & 1
Whether it's a power of two using (num & (num - 1)) == 0
"""

num = int(input("Enter an integer: "))

is_even = (num & 1) == 0
is_power_of_two = num > 0 and (num & (num - 1)) == 0

print(f"\nNumber: {num}")
print(f"Even: {is_even}")
print(f"Power of two: {is_power_of_two}")
