age=input("Enter your age: ")
license_of_the_user=input("Do you have a driving license? (yes/no): ")
age_of_the_user=int(age)
license=str(license_of_the_user)



if age_of_the_user >= 22 and license == "yes":
      print("✅ you are eligible to drove.")
elif age_of_the_user <= 22 and license == "yes":
      print("❌ You are not eligible — you must be at least 22 years old.")  
elif age >= 22 and license =="no":
      print("❌ You are not eligible — you don't have the license that required.")
else:
      print("❌ You are not eligible — you must be at least 22 and have a valid driving license.")
