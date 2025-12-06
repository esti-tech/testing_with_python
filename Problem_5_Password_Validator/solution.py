print("=== Password Strength Checker ===")
password = input("Enter your password: ")

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|" for c in password)

if len(password) < 8:
    print("❌ Password must be at least 8 characters long.")
elif not has_upper:
    print("❌ Password must include at least one uppercase letter.")
elif not has_lower:
    print("❌ Password must include at least one lowercase letter.")
elif not has_digit:
    print("❌ Password must include at least one number.")
elif not has_special:
    print("❌ Password must include at least one special character.")
else:
    print("✅ Strong password! Good job.")
