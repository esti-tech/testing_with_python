"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""# Parity and Power Detector.py

"""
***
Objective: Use bitwise operations to check an integer.
1. Determine if the number is even or odd (parity).
2. Determine if the number is a power of two.
***
"""

# --- Input an integer. ---
try:
    # Get user input and convert it to an integer.
    num = int(input("Enter an integer to check its parity and power of two status: "))

except ValueError:
    print("Invalid input. Please enter a whole number.")
    # Exit the script if the input is not a valid integer
    exit()

# --- Parity Check (Even or Odd) ---

# A number is odd if its least significant bit (LSB) is 1.
# The bitwise AND operation: num & 1 checks the LSB.
# If LSB is 1 (odd), the result is 1 (True). If LSB is 0 (even), the result is 0 (False).
is_odd = num & 1

print("\n--- Parity Check ---")

# Check the result of the bitwise AND operation
if is_odd:
    print(f"The number {num} is Odd.")
else:
    print(f"The number {num} is Even.")

# --- Power of Two Check ---

# A positive number is a power of two (1, 2, 4, 8, 16, etc.) if and only if 
# it has exactly one '1' bit in its binary representation.

# For any power of two (e.g., 8 is 1000 in binary), the number immediately before it 
# (e.g., 7 is 0111 in binary) will have all the lower bits set.
# The bitwise AND of num & (num - 1) will always be 0 for a power of two.
# Example: 8 (1000) & 7 (0111) = 0000

print("\n--- Power of Two Check ---")

if num > 0 and (num & (num - 1)) == 0:
    print(f"The number {num} IS a power of two.")
else:
    print(f"The number {num} IS NOT a power of two (or is non-positive).")

print("------------------------------------------")

# Optional: Print binary representation for better understanding
print(f"Binary of {num}: {bin(num)}")
