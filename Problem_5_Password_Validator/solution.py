name = input("enter your name:\n")
passw = input("enter password:\n")
if len(passw) >= 8:
    if passw.lower() != name.lower():
        if any(i.isdigit() for i in passw):
            if any(u.isupper() for u in passw):
                print("strong password!")
            else: print("the password must contain at least one uppercase letter.")    
        else: print("the password must contain at least 1 digit.")
    else: print("Password can not be the same as your name.")
else: print("the length of password must be at least 8 characters.")
