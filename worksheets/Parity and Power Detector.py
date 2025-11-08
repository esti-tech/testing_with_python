
num = int(input("Enter an integer: "))

if num & 1:
    print("The number is odd.")
else:
    print("The number is even.")

if num > 0 and (num & (num - 1)) == 0:
    print("The number is a power of two.")
else:
    print("The number is NOT a power of two.")