# your code here
name = input("Enter your name: ")
password = input("Enter your password: ")
errors = []
if len(password) < 8:
    errors.append("Password must be at least 8 characters long.")
if not any(ch.isdigit() for ch in password):
    errors.append("Password must contain at least one number.")
if password.lower() == name.lower():
    errors.append("Password should not be the same as your name")
if len(errors) == 0:
    print("Strong password!")
else:
    print("Weak password. Please fix the following:")
    for error in errors:
        print("-", error)

