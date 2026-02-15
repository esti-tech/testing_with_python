# Bit Masking Practice.py
num = int(input("Enter a number: "))
bit = int(input("Enter bit position to work on (0 for least significant bit): "))

mask = 1 << bit  
if num & mask:
    print(f"Bit {bit} is set (1).")
else:
    print(f"Bit {bit} is not set (0).")

set_num = num | mask
print(f"After setting bit {bit}: {set_num} (binary: {bin(set_num)})")

clear_num = num & ~mask
print(f"After clearing bit {bit}: {clear_num} (binary: {bin(clear_num)})")

toggle_num = num ^ mask
print(f"After toggling bit {bit}: {toggle_num} (binary: {bin(toggle_num)})")
