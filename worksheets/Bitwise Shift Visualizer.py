
# Input from user
num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))

print(f"\nOriginal number: {num}")
print(f"Binary form: {bin(num)}")

# Left shift
left_shifted = num << shift
print(f"\nAfter left shift by {shift}: {left_shifted}")
print(f"Binary form: {bin(left_shifted)}")

# Right shift
right_shifted = num >> shift
print(f"\nAfter right shift by {shift}: {right_shifted}")
print(f"Binary form: {bin(right_shifted)}")
