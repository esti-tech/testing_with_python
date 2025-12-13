            """

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""
num = int(input("Enter an integer: "))

# Even or Odd using bitwise AND
if num & 1 == 0:
    print("Even")
else:
    print("Odd")

# Power of Two using bitwise trick
if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not power of 2")