# Password Strength Checker
name = input("Enter your name: ")
password = input("Enter your password: ")
missing = []

if len(password) < 8:
    missing.append("at least 8 characters")
if not any(c.isdigit() for c in password):
    missing.append("at least one digit")
if password.lower() == name.lower():
    missing.append("should not be the same as your name")
if not missing:
    print("Strong password!")
else:
    print("Weak password. Missing rules:")
    for rule in missing:
        print("-", rule)
