# your code here
# my code
name = input("what is your name(user name)? ")
password = input("please input your password? " )

unfulfilled_rules = [] 
if len(password) < 8:
     unfulfilled_rules.append("password must be at least 8 characters")

if password == name:
  unfulfilled_rules.append("Cannot be same as your name")

  
has_number = False

if "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
    has_number = True

if not has_number:
   unfulfilled_rules.append("password must contain at least one number")

if unfulfilled_rules :
    print("unfulfilled  requirements:")
    for rule in unfulfilled_rules:
        print(rule)


rules_passed = 3 - len(unfulfilled_rules)

if rules_passed == 3:
    print("STRONG PASSWORD! ✓")
elif rules_passed == 2:
    print("MEDIUM STRENGTH PASSWORD")
elif rules_passed == 1:
    print("WEAK PASSWORD")
else:
    print("VERY WEAK PASSWORD")

     
