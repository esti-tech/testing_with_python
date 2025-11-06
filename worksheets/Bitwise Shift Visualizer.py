"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
num = int(input("Enter an integer: "))
shift_positions = int(input("Enter number of shift positions: "))

print("\nOriginal integer:", num)
print("Binary form:", bin(num))

left_shifted_num = num << shift_positions
print(f"\nLeft shift by {shift_positions} positions:")
print("Result:", left_shifted_num)
print("Binary form:", bin(left_shifted_num))

right_shifted_num = num >> shift_positions
print(f"\nRight shift by {shift_positions} positions:")
print("Result:", right_shifted_num)
print("Binary form:", bin(right_shifted_num))
