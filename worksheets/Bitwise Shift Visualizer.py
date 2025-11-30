num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))

print("\nBefore shift:")
print(f"Binary: {bin(num)}")

left_shift = num << shift
print("\nAfter left shift:")
print(f"Binary: {bin(left_shift)}")
print(f"Decimal: {left_shift}")

right_shift = num >> shift
print("\nAfter right shift:")
print(f"Binary: {bin(right_shift)}")
print(f"Decimal: {right_shift}")
