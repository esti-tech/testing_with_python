
num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))

print(f"\nOriginal number: {num}")
print(f"Binary: {bin(num)}")


left_shifted = num << shift
print(f"\nAfter left shift by {shift}: {left_shifted}")
print(f"Binary: {bin(left_shifted)}")


right_shifted = num >> shift
print(f"\nAfter right shift by {shift}: {right_shifted}")
print(f"Binary: {bin(right_shifted)}")