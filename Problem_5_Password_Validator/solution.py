password = input("Enter password: ")

# Check criteria
length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

if length_ok and has_upper and has_lower and has_digit:
    print("Password is strong! ✅")
else:
    print("Password is weak! ❌")
    if not length_ok:
        print("- Must be at least 8 characters")
    if not has_upper:
        print("- Must contain uppercase letter")
    if not has_lower:
        print("- Must contain lowercase letter")
    if not has_digit:
        print("- Must contain a digit")
