#Problem 5:Password Validator

print("===password strength Validator===")
password = input("Enter Your Password:")

#Check password strength
has_upper=any(char.isupper() for char in password)
has_lower=any(char.islower() for char in password)
has_digit=any(char.isdigit() for char in password)
has_special=any(not char.isalnum() for char in password)
is_long_enough=len(password)>=8

#Check all condition
if is_long_enough and has_upper and has_lower and has_digit and has_special:
  print("Strong Password!All Requirements Met.")
else:
  print("Weak Password!Missing Requirements:")

#Show exactly what's missing
if not is_long_enough:
  print("-At least 8 characters")
if not has_upper:
  print("-At least one uppercase letter (A-Z)")
if not has_lower:
  print("-At least one lowercase letter (a-z)")
if not has_digit:
  print("-At least one digit (0-9)")
if not has_special:
  print("-At least one special character (!@#$%^& etc.)")
  
    
