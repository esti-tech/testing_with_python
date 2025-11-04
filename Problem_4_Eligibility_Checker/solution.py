#Problem 4:Eligibility checker

print("=== Role Eligible Checker ===")

#Get user input
age = int(input("Enter your age:"))
has_license = input("Do you have a valid license? (yes or no):").lower().strip()

#Check eligibility-Both condition must be true
if age >=18 and (has_license == "yes" or has_license == "y"):
  print("Congratulation!You are ELIGIBLE for the role.")
  print("You meet both requirements:age 18+ and valid license.")
else:
  print("sorry,You are not ELIGIBLE.")

#explain why
if age <18:
  print("Reason: You must be at least 18 years old.")
  if has_license not in ["yes" , "y"]:
    print("Reason: You need a valid license.")
    
  
  
