# Parity and Power of Two Detector

number = int(input("Enter an integer: "))
if number & 1 == 0:
    print(f"{number} is even.")
else:  
    print(f"{number} is odd.")

if number & (number - 1) == 0:
    print(f"{number} is a power of two.")
else:
    print(f"{number} is not a power of two.")