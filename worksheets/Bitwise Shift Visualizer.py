"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
num = int(input("Number: "))
print(f"Left shift: {num << 1} - {bin((num << 1))}")
print(f"Right shift: {num >> 1} - {bin((num >> 1))}")