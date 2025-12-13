# ask input from user
age=int(input("enter yours age"))
license=input("do you have the required license?(yes/no):")
#check eligibility
if age >= 18 :
   if license=="yes":
      print("you are eligiable for this")
   elif license=="no":
      print("you are not eligeable for this")  
   else:
      print("incorrect choice select yes or no")
else:
   print("you are not eligiable:at least your age is 18 ")
