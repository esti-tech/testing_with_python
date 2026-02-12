name = input("Your name: ")
password = input("Password: ")

missing = []
if len(password) < 8:
    missing.append("Password too short")
if not any(ch.isdigit() for ch in password):
    missing.append("Add at least one number")
if password.lower() == name.lower():
    missing.append("Password can't be your name")

if not missing:
    print("Password is strong")
elif len(missing) == 1:
    print("Password is okay, fix 1 thing:", missing[0])
else:
    print("Password is weak, fix these:", ", ".join(missing))