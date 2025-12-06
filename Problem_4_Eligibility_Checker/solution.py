print("=== Eligibility Checker ===")

age = int(input("Enter your age: "))
has_license = input("Do you have a valid driver's license? (yes/no): ").lower()

if age >= 18 and has_license == "yes":
    print("✅ You are eligible for the role!")
elif age >= 18 and has_license == "no":
    print("❌ You meet the age requirement but need a license to qualify.")
else:
    print("❌ You are not eligible. You must be at least 18 years old and have a license.")
