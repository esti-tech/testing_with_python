name = input("Enter your name: ")
password = input("Enter your password: ")
if len(password) < 8:
    print(" Password must be at least 8 characters long.")

elif not any(ch.isdigit() for ch in password):
    print("Password must contain at least one number.")

elif password.lower() == name.lower():
    print("Password should not be the same as your name.")

else:
    print("Strong password!")
