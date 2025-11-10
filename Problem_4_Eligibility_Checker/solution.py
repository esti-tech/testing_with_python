
age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ")


if age >= 18:
    if has_license.lower() == "yes":
        print("✅ You are eligible to drive.")
    else:
        print(" You need a driving license to drive.")
else:
    print(" You are not old enough to drive.") your code here
