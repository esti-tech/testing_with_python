# Bitwise Shift Visualizer

number = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))

print("\nbefore shifting:")
print(f"Original number: {number}")
print(f"binary form: {bin(number)}")

print("\nAfter left shift:")
l_shifted = number << shift
print(f"Left shift: {l_shifted}")
print(f"binary form: {bin(l_shifted)}")

print("\nAfter right shift:")
r_shifted = number >> shift
print(f"Right shift: {r_shifted}")
print(f"binary form: {bin(r_shifted)}")