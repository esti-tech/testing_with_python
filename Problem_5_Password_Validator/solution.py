# Password Strength Checker App
password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

# I'm keeping the special character list short for simplicity
special_chars = "!@#$%&*^~"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

    # Check each rule individually and give feedback
if len(password) < 8:
    print("-Password must be at least 8 characters.")
if not has_upper:
    print("-Password must include an uppercase letter.")
if not has_lower:
    print("-Password must include a lowercase letter.")
if not has_digit:
    print("-Password must include a number.")
if not has_special:
    print("-Password must include a special character(!@#$%&*^~).")

    # If all rules are satisfied
if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password!")
