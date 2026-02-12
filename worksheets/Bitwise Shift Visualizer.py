"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
n = int(input("Enter a number: "))
s = int(input("Enter shift positions: "))

print("Before shift:", bin(n))
print("Left shift:", bin(n << s))
print("Right shift:", bin(n >> s))