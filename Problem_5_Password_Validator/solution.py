name=(input("what is your name?   "))
password=input(" you shoud not have to make your passwor similar to your name enter your password:  ") 

if len(password)>=8:

    if any(char.isdigit() for char in password):

        if name.lower() not in password.lower():
            print("Stength: highly strong")
            print("password passed all requirements")
        else:
            print("stength: Medium")
            print("password should not be contain your name and you didnot listen me so your password is becoming less effective")

    else:
        print("Strength: Neutral")
        print("password must contain at least one digit (0-9)")

else:
    print("Strength: very weak")
    print("password must be atleast 8 characters long")