age = int(input("Enter your age: "))
license_status = input("Do you have a driving license? (yes/no): ").strip().lower()

if age >= 18:
    if license_status == 'yes':
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive without a license.")
else:
    print("You are not eligible to drive due to age restrictions.")