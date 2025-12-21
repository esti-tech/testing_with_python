# Boolean Puzzle Game

print("Is the user verified?")
print("1. True")
print("0. False")
verify=bool(int(input()))

if verify == True:
    id=int(input("Enter user ID: "))
    if id & 1 == 0:
        flag=int(input("Enter security flag bits in number: "))
        if flag & 0b111 != 0:
            print("Access Granted")
        else:
            print("Access Denied: Security flag bits do not meet the criteria.")
    else:
        print("Access Denied: User ID is not even.")
else:
    print("Access Denied: User is not verified.")