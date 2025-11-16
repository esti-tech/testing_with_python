# Eligibility Checker App

age = int(input("Enter your age:"))
has_license = input("Do you have a license? (yes/no):").lower()
if age >= 18 and has_license == "yes":
    print("You are eligible for this role.")
elif age < 18 and has_license == "yes":
    print("Sorry, you are too young for this role.")
elif age >= 18 and has_license != "yes":
    print("Sorry, you need a license to be eligible.")
else:
    print("Sorry, you are not eligible for this role.")
