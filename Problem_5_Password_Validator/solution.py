
name=(input("what's your name? "))
password=input("enter your password: ") 

if len(password)>=8:

    if any(char.isdigit() for char in password):

        if name.lower() not in password.lower():
            print("Stength: strong")
            print("password passed all requirements")
        else:
            print("stength: Medium")
            print("password should not contain your name")

    else:
        print("Strength: Neutral")
        print("password must contain at least one digit (0-9)")

else:
    print("Strength: weak")
    print("password must be atleast 8 characters long")
        

