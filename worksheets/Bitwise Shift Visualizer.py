"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
num = int(input("Enter an integer:"))
shift = int(input("Enter number of shift positions:"))
left_shift = num << shift
right_shift = num >> shift
print(f"\nOriginal number: {num} -> {bin(num)}")
print(f"Left shift by {shift}: {left_shift} -> {bin(left_shift)}")
print(f"Right shift by {shift}: {right_shift} -> {bin(right_shift)}")
