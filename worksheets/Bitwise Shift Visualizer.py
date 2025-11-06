"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""

num = int(input("Enter an integer: "))
shift = int(input("Enter shift positions: "))

print(f"\nOriginal number: {num}")
print(f"Binary: {bin(num)}")

left_shift = num << shift
right_shift = num >> shift

print(f"\nAfter left shift by {shift}: {left_shift}")
print(f"Binary: {bin(left_shift)}")

print(f"\nAfter right shift by {shift}: {right_shift}")
print(f"Binary: {bin(right_shift)}")
