"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""
num = int(input("Number: "))
if num & 1 == 0: print("Even.")
else: print("odd. ")
if (num & (num - 1)) == 0: print("Power of 2. ")
else: print("Not a power of 2. ")