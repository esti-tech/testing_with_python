"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""

num = int(input("Enter a number: "))

if num & 1:
    print("The number is odd.")
else:
    print("The number is even.")

if num > 0 and (num & (num - 1)) == 0:
    print("The number is a power of two.")
else:
    print("The number is not a power of two.")