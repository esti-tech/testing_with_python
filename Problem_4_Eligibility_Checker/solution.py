#1. Get age and license status.
age=int(input("enter your age:"))
has_license=input(" do you have a driving license?(yes/no):").lower()
#2. Use nested if/else to check eligibility.
if age>=18:
  if has_license=="yes":
    print(" you are eligible to drive.")
  else:
   print ("you are old enough, but you need a driving license.")
else:
 print("you are not eligible to drive yet.")
#3. Print result.
