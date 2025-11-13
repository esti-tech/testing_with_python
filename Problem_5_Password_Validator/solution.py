# 1. Ask for name and password
name = input("Enter your name: ")
password = input("Enter your password: ")

# 2. Check conditions
length_ok = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
not_same_as_name = password != name

# 3. Check strength 
if length_ok and has_digit and not_same_as_name:
    print("Password is strong.")
elif not length_ok and not has_digit and not not_same_as_name:
    print(" Weak password: Too short, no digits, and same as your name.")
elif password>=8:
    print("the password is normal")
else:
    print("Something went wrong.")
