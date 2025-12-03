age = int(input("Enter your age: "))
license_check = input("Do you have a valid driver's license? (yes/no): ")

#to check the person has only yes or no input
if license_check not in ["yes", "no"]:
    print("Invalid input! Please type only 'yes' or 'no'.")
else:
    print(f"you answered: {license_check}")
if age >= 18 and license_check == "yes":
    print("You are eligible for a driving role.")

# If the person is over 18 but doesn't have a license
elif age > 18 and license_check == "no":
    print("You can obtain a valid driver's license to be eligible for a driving role.")

# If the person is under 18 years old but it has a license to unfold that is illegal
elif age < 18 and license_check == "yes":
    print("you need to be at least 18 years old to be eligible for a driving role.")
else:
    print("You are not eligible for a driving role.")
