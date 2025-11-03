
name = input("Enter your name: ")
password = input("Enter your password: ")

if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        if password != name:
            print("Strong password!")
        else:
            print("Password should not be the same as your name.")
    else:
        print("Password should have at least one number.")
else:
    print("Password should be at least 8 characters long.")
