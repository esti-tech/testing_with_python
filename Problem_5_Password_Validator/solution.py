print(" Creat a strong password that contains at least: ")
print("      - have 5 characters (long)")
print("      - One uppercase letter")
print("      - One lowercase letter")
print("      - One digit")
print("      - One special character")
#-------------------------------------------------------
password=input("Enter your password: ")
length =  len(password)
if not len(password) > 5:
    print("❌ Weak: Password must be at least 5 characters long.")
if not any(char.isupper() for char in password):
    print("❌ Weak: The Password must Contain at least one uppercase letter.")   
if not any(char.islower() for char in password):
    print("❌ Weak: The Password must Contain at least one lowercase letter.")
if not any(char.isdigit() for char in password):
    print(" ❌ Weak: The Password must Contain at least one digit.")
if not any(char in ' !@#$%^&*()-_=+[]{}|;:",.<>?/`~' for char in password):
    print("❌ Weak: The Password must Contain at least one special character.")
else:
    print("✅ Strong password!")
