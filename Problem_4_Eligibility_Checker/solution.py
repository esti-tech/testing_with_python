print("Eligibility_Checker")
age = int(input("Enter your age: "))
license_status = input("Do you have a valid license? (yes/no): ").lower()

if age >= 18:
    if license_status == "yes":
        print("You are eligible for the role.")
    else:
        print("You must have a valid license to be eligible.")
else:
    print("You are not old enough for the role.")
