"""
Bitwise Shift Visualizer
Input an integer and number of shift positions.
Show results of left shift and right shift.
Print the binary form before and after.
"""
num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))
left_shift = num << shift
right_shift = num >> shift
print("\nBefore shifting:")
print(f"Decimal: {num}")
print(f"Binary : {bin(num)}")
print("\nAfter left shift:")
print(f"Decimal: {left_shift}")
print(f"Binary : {bin(left_shift)}")
print("\nAfter right shift:")
print(f"Decimal: {right_shift}")
print(f"Binary : {bin(right_shift)}")
