# your code here
name = input("Enter your name: ")
password = input("Enter your password: ")
missing_rules = []
if len(password) < 8:
    missing_rules.append("Password must be at least 8 characters long.")
if not any(char.isdigit() for char in password):
    missing_rules.append("Password must contain at least one digit.")
if password.lower() == name.lower():
    missing_rules.append("Password should not be the same as your name.")
if not missing_rules:
    print(" Password is strong!")
else:
    print(" Password is weak.")
    print("Missing rules:")
    for rule in missing_rules:
        print("-", rule) 
