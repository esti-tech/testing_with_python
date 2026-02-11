age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no): ").lower()

if age >= 18 and has_license == "yes":
    print("You are eligible for the role!")
else:
    print("You are not eligible for the role.")
    if age < 18:
        print("Reason: Too young (must be 18 or older)")
    if has_license != "yes":
        print("Reason: License required")
