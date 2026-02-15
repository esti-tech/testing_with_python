 patch-1
# your code here
name = input("Enter your name: ")
password = input("Enter your password: ")
missing_rules = []
if len(password) < 8:
    missing_rules.append("Password must be at least 8 characters long.")
if not any(char.isdigit() for char in password):
    missing_rules.append("Password must contain at least one digit.")
if password.lower() == name.lower():
    missing_rules.append("Password should not be the same as your name.")
if not missing_rules:
    print(" Password is strong!")
else:
    print(" Password is weak.")
    print("Missing rules:")
    for rule in missing_rules:
        print("-", rule)

username=input("Enter your user name: ")
password=input("Enter your password: ")
rule_correct=0
if len(password)>=8:
    rule_correct +=1
else:
    print("Password must be graterthan or equal to 8 digits.")
if password !=username:
    rule_correct +=1
else:
    print("password can not be the same as username.")
has_digit = any(char.isdigit() for char in password )
if has_digit:
    rule_correct +=1
else:
    print("password must be contain at least one digit")
if rule_correct ==3:
    print("The password is strong.")
elif rule_correct ==2:
    print ("The password is meadium.")
elif rule_correct ==1:
    print("The password is weak.")
else:
    print("Your password not fulfill this requirment.")
patch-1
