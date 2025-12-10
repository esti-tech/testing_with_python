# Bit masking practice

num =int(input("Enter a number:"))
bit =int(input("Enter bit position:"))

print("\noriginal:",bin(num))
print("Check bit (is it 1?):",num & (1<<bit))
print("Set bit (turn to 1):",bin (num| (1<<bit)))
print("Clear bit (turn to 0):",bin (num &~ (1<<bit)))
print("Toggle bit (flip 1 to 0 or 0 to 1):",bin (num ^ (1<<bit)))
