 age = int(input("please enter your age "))
if age < 21:
    print("warning you are under age of 21")
else:
    license = str(input("do you have a license (yes/no) "))
    if license == "yes" :
       pro = str(input("which one is your profession (loader/excavater/roller)"))
       if pro == "loader" :
          print("sorry, we only need excaveton professionals")
       elif pro == "excavater" :
          print("you are eligeble for the job")
       elif pro == "roller" :
          print("sorry, we only need excaveton professionals")
       else:
          print("Error, unknown profession")
    else:
         print("Error, please taype yes/no only")