

print("This code checks ih your password is strong or weak")
print("enter your name: ")
name = input()
print("enter your password: ")
password = input()
missed_rules = ""
if len(password) < 8:
    missed_rules += "the password must be at least 8 characters long\n"
digits = "0123456789"
if not (
    "0" in password or
    "1" in password or
    "2" in password or
    "3" in password or
    "4" in password or
    "5" in password or
    "6" in password or
    "7" in password or
    "8" in password or
    "9" in password
):
    missed_rules += "Password must contain at least one digit.\n"
if password == name.lower():
    missed_rules += "Password mustnot be the same as your name.\n"
if missed_rules =="":
    print("password is valid and strong\n")
else:
    print("yourpassword is weak\n" + missed_rules)
