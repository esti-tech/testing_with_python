"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""
num = int(input("Enter an integer: "))

if num == 0:
    print("0 is neither even nor odd")
elif num & 1  == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a power of two")
else:
    print(f"{num} is not a power of two")
