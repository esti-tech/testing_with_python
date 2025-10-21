# Program to check password strength

name = input("Enter your name: ")
password = input("Enter your password: ")


if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if password != name:
            print("✅ Strong password! It meets all the criteria.")
        else:
            print("❌ Password should not be the same as your username.")
    else:
        print("❌ Password must contain at least one digit.")
else:
    print("❌ Password must be at least 8 characters long.")
