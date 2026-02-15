 patch-1
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

#Eligiblity checker for car rental service.
age=int(input("Enter your age: "))
if age>=21:
    license=input("Do you have a license? ") 
    if license == "yes": #all letters are must be small letter.
        print("You are Eligiable to car rental.") 
    else:
        print("You are not eligiable for car rental")
else:
    print("You are not Eligiable for car rental.")
patch-1