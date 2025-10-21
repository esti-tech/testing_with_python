
num = int(input("Enter a number: "))
bit = int(input("Enter bit position: "))

mask = 1 << bit


if num & mask:
    print("Bit is 1")
else:
    print("Bit is 0")
