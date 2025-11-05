
age = int(input("Enter your age: "))
license_status = input("Do you have a driving license? (yes/no): ")

if age >= 18:
    if license_status == "yes":
        print("You can drive.")
    else:
        print("You cannot drive because you don't have a license.")
else:
    print("You cannot drive because you are under 18.")