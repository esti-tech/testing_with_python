
age = int(input("Enter your age: "))
license_status = input("Do you have a driving license? (yes/no): ")

if age >= 18:
    if license_status.lower() == "yes":
        print("You are eligible to drive.")
    else:
        print("You need a driving license to drive.")
else:
    print("You are not old enough to drive.")