print("=== Simple Bit Masking Practice ===")

while True:
    print("\n1. Check bit")
    print("2. Set bit")
    print("3. Clear bit")
    print("4. Toggle bit")
    print("5. Count bits set to 1")
    print("6. Exit")

    choice = input("Choose (1-6): ")

    if choice == "6":
        print("Goodbye!")
        break

    num = int(input("Enter an integer: "))
    print(f"Binary: {bin(num)}")

    if choice in ["1", "2", "3", "4"]:
        pos = int(input("Enter bit position (starting from 0): "))

    if choice == "1":  # Check bit
        print("Bit is:", "1 (set)" if num & (1 << pos) else "0 (clear)")

    elif choice == "2":  # Set bit
        num = num | (1 << pos)
        print("After setting:", num, "Binary:", bin(num))

    elif choice == "3":  # Clear bit
        num = num & ~(1 << pos)
        print("After clearing:", num, "Binary:", bin(num))

    elif choice == "4":  # Toggle bit
        num = num ^ (1 << pos)
        print("After toggling:", num, "Binary:", bin(num))

    elif choice == "5":  # Count set bits
        print("Bits set to 1:", bin(num).count("1"))

    else:
        print("Invalid choice!")