name=input("Enter your name: ")
password_input = input("Enter your password: ")
error= []
if len(password_input) < 8:
    error.append("Password must be at least 8 characters long.")
if not any(char.isdigit() for char in password_input):
    error.append("Password must contain at least one number.")
if not any(char.isupper() for char in password_input):
    error.append("Password must contain at least one uppercase letter.")
if not any(char.islower() for char in password_input):
    error.append("Password must contain at least one lowercase letter.")
if not any(char in "!@#$%^*()_+-=" for char in password_input):
    error.append("Password must contain at least one special character.")

if error:
    print("Password is invalid:")
    for err in error:
        print(" -", err)
else:
    print("Password is valid.")