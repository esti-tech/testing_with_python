# Ask user for an integer
num = int(input("Enter an integer:"))
# mask to extract only the last 4 bits
mask = 0b1111
# Apply bitwise AND to keep only 4 bits
result = num & mask
print(f"Binary of {num}: {bin(num)}")
print(f"After applying mask {bin(mask)}: {bin(result)}")
