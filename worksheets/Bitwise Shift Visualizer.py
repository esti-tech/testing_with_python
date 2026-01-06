"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
num = int(input("Enter an integer: "))
shift_positions = int(input("Enter number of shift positions: "))
print(f"Original: {num} (Binary: {bin(num)})")
print(f"(After Left Shift: {bin(num << shift_positions)})")
print(f"(After Right Shift: {bin(num >> shift_positions)})")
print(f"Left_shift: {num << shift_positions} (Binary: {bin(num << shift_positions)})")
print(f"Right_shift: {num >> shift_positions} (Binary: {bin(num >> shift_positions)})")

