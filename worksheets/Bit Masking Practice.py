# Bit Masking Practice.py

print("Welcome to Bit Masking Practice ")

x = 0
print("Start value:", x, "in binary:", bin(x))

x = x | (1 << 2)
print("\nSet bit 2 →", x, "binary:", bin(x))

x = x ^ (1 << 1)
print("Toggle bit 1 →", x, "binary:", bin(x))

x = x & ~(1 << 2)
print("Clear bit 2 →", x, "binary:", bin(x))

bit_value = (x >> 1) & 1
print("Bit 1 value is:", bit_value)

print("\nBit practice done ")
