age = int(input("enter your age:\n"))
license = input("Do you have a license?(yes/no)\n").lower()
if age >= 18 and license in ["yes", "y"]:
     print("you are eligible. good luck!🤞🏽")
else: print("sorry! you are not eligible.🙏")
        


