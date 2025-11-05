# your code here
# my code
print("welcome to ethiovote validator".upper())
print("we will check your eligibility status to vote ethiopian 2026 election!")
age = int(input("please input your age? " ))


if age >= 18:

  license_status = input("Do you have NATIONAL ID (FAYDA)? type yes or no: ")
  
  if license_status == "yes":
     print("you are eligible to vote".upper())
  elif license_status == "no":
    
     print("you are not eligible to vote".upper())
  else:
        
     print("invalid license status please return.".upper())         
else:
    print("you are not eligible to vote".upper())








      
