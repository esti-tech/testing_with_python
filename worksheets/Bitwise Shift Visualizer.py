
num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))

print(f"\nOriginal number: {num}")
print("Binary form:", format(num, '08b'))  

left = num << shift
right = num >> shift

print(f"\nAfter left shift by {shift}:")
print(f"Decimal: {left}")
print("Binary :", format(left, '08b'))

print(f"\nAfter right shift by {shift}:")
print(f"Decimal: {right}")
print("Binary :", format(right, '08b'))

