#accept input from user
id=int(input("enter your id:"))
have_verified=input("are you verified?yes/no: ")
verified=have_verified=="yes"
flags = int(input("Enter your security flag (as a number): "))
if verified == True and id & 1 == 0 and flags & 0b111 != 0:
     print("access is granted")
else:
     print("access is not granted")     