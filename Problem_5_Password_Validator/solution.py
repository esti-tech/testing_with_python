name = input("Enter your name: ")
password = input("Enter your password: ")

errors = []
if len(password) < 8:
    errors.append("Password must be at least 8 characters")
if not any(ch.isdigit() for ch in password):
    errors.append("Password must contain a digit")
if password == name:
    errors.append("Password cannot be the same as your name")

if errors:
    print("Weak password. Fix these:", ", ".join(errors))
else:
    print("Password is strong! Good job!")