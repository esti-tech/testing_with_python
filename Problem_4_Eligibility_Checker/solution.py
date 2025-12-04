age=int(input("how old are you? "))
if age>=18:
    print("age requirement: pass")
    print("licence status checker: ")
    choice=input("do you have a license? yes/no ")
        
    if choice == "yes":
        print("valid")
        print("congratulations! you are legal")
              
    else:
        print("invalid")
        print("sorry! you are not legal")
            
else:
    print("age requirement: failed")
    print("sorry! you are not legal ")