"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""
patch-1
num = int(input("Input an integer: "))
if num & 1 == 0:
    print("even")
else:
    print("odd")
if num > 0 and (num & (num - 1)) == 0:
    print("is a power of two")
else:
    print("is not a power of two")

num = int(input("Enter an integer: "))
if num & 1:
    print(f"{num} is Odd")
else:
    print(f"{num} is Even")
if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a Power of Two")
else:
    print(f"{num} is NOT a Power of Two")
patch-1
