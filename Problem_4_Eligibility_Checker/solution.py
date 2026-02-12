# Program to check eligibility for a role based on age and license status

age = int(input("Enter your age: "))
has_license = input("Do you have a valid driving license? (yes/no): ").lower()

if age >= 25:
    if has_license == "yes":
        print("✅ You are eligible for the role.")
    else:
        print("❌ You are not eligible because you don't have a valid license.")
else:
    print("❌ You are not eligible because you are under 18.")
