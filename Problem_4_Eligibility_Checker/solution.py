
age=int(input("how old are you? "))
licence_num= "1234"

if age>=18:
    print("age requirement: passed")
    print("licence status checker: ")
    user_licence=input("enter your licence number: ")
        
    if user_licence == licence_num:
        print("licence status: valid")
        print("congratulations! you are eligible")
              
    else:
        print("licence status: invalid")
        print("sorry! you are not eligible")
            
else:
    print("age requirement: failed")
    print("sorry! you are not eligible")

