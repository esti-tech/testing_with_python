#1. Ask for name and password.
def password_validation ():
  name=input("enter your name :")
  password =input("enter your password:")
  missing_rule=[]
#2. Check length
  if len(password)<8:
     missing_rule.append("password should be at least 8 char long.")
#3check for digit
  if not any (char.isdigit() for char in password):
      missing_rule.append("password should contain at least one digit.")
#4 check not the same as
  if password.lower()==name.lower():
     missing_rule.append("password should not be the same as your name.")
#. Output
  if not missing_rule:
   print("password strength:strong")
  else:
   print("password streangth: weak")
  print("missing rules:")
  for rule in missing_rule:
     print("-",rule)
password_validation()
