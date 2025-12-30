def check_eligibility(age, has_license):
    if age >= 18 and has_license.lower() == 'yes':
        return True
    else:
        return False
age = int(input("Enter your age: "))
has_license = input("Do you have a valid driver's license? (yes/no): ")
if check_eligibility(age, has_license):
    print("Congratulations! You are eligible for the role.")
else:
    print("Sorry, you are not eligible for the role.")
