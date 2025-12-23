#Eligibility checker
Age = int(input("Enter your age: "))
license_status = input("Do you have a valid license? (YES/NO): ").upper()

if Age >= 18:
    if license_status == "YES":
        print(" You are eligible for the role.")
    else:
        print(" You are not eligible , you must have a valid license.")
else:
    print(" You are not eligible , you must be at least 18 years old.")
