"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
# bitwise_shift_visualizer.py

print("=== Bitwise Shift Visualizer ===")

# Get input from the user
num = int(input("Enter an integer: "))
shifts = int(input("Enter number of shift positions: "))

print("\n--- Original Value ---")
print(f"Decimal : {num}")
print(f"Binary  : {bin(num)}")

# Left shift
left_shifted = num << shifts
print("\n--- After Left Shift ---")
print(f"{num} << {shifts} = {left_shifted}")
print(f"Binary  : {bin(left_shifted)}")

# Right shift
right_shifted = num >> shifts
print("\n--- After Right Shift ---")
print(f"{num} >> {shifts} = {right_shifted}")
print(f"Binary  : {bin(right_shifted)}")