# your code here
age = int(input("Please enter your age: "))
has_license = input("Do you have a license? (yes/no): ").lower() == 'yes'
if age >= 18:
    if has_license:
        result = "You are eligible."
    else:
        result = "You are not eligible. You need a license."
else:
    result = "You are not eligible. You must be at least 18 years old."
print(result)
