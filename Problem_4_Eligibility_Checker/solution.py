# your code here
age = int(input("Enter your age: "))
license_status = input("Do you have a driving license? (yes/no): ")

if age < 18:
    print("You are too young to drive.")
else:
    if license_status == "yes":
        print("You are eligible to drive.")
    else:
        print("You need a license to drive.")
