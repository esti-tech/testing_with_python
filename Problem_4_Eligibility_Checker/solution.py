# Get age and license status.
age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ").strip().lower()

# Use nested if/else to check eligibility.
if age >= 18:
    # Check 1: Must be 18 or older
    if has_license == "yes":
        # Check 2: Must have a license
        print("You are eligible to drive.")
    else:
        # Check 2 (Fail): Older than 18, but no license
        print("You need a driving license to drive.")
else:
    # Check 1 (Fail): Not old enough
    print("You are not old enough to drive.")