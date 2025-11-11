def shift_operations(num, shift_positions):
    left_shifted = num << shift_positions
    right_shifted = num >> shift_positions
    original_binary = bin(num)[2:]  # Strip the '0b' prefix
    left_shifted_binary = bin(left_shifted)[2:]
    right_shifted_binary = bin(right_shifted)[2:]
    print(f"Original number: {num}")
    print(f"Binary representation (before): {original_binary}")
    print(f"Left shifted by {shift_positions} positions: {left_shifted}")
    print(f"Binary after left shift: {left_shifted_binary}")
    print(f"Right shifted by {shift_positions} positions: {right_shifted}")
    print(f"Binary after right shift: {right_shifted_binary}")
num = int(input("Enter an integer: "))
shift_positions = int(input("Enter the number of shift positions: "))
shift_operations(num, shift_positions)
