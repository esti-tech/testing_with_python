number = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))
binary_before = bin(number)[2:]
left_shifted = number << shift
binary_left = bin(left_shifted)[2:]
right_shifted = number >> shift
binary_right = bin(right_shifted)[2:]
print("\nOriginal number:")
print(f"Decimal: {number}")
print(f"Binary : {binary_before}")

print("\nAfter left shift (<<):")
print(f"Decimal: {left_shifted}")
print(f"Binary : {binary_left}")

print("\nAfter right shift (>>):")
print(f"Decimal: {right_shifted}")
print(f"Binary : {binary_right}")
