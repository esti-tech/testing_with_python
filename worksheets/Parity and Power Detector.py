"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""

num = int(input("Enter an integer:"))

# check if a number is even/odd
if num & 1 == 0:
    print("Even number")
else:
    print("odd number")
# check if it's a power of two
if num > 0 and (num & (num - 1)) == 0:
    print("It is a power of two")
else:
    print("Not a power of two")
