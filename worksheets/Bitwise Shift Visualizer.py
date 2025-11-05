"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
# Program to perform left and right bitwise shifts

# Input integer and shift count
num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))

# Display original binary
print(f"\nOriginal number: {num}")
print(f"Binary form: {bin(num)[2:]}")

# Perform shifts
left_shift = num << shift
right_shift = num >> shift

# Display results
print("\n--- Left Shift ---")
print(f"Result: {left_shift}")
print(f"Binary: {bin(left_shift)[2:]}")

print("\n--- Right Shift ---")
print(f"Result: {right_shift}")
print(f"Binary: {bin(right_shift)[2:]}")
