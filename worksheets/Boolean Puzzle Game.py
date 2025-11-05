verified = True  

user_id = int(input("Enter your user ID: "))
flags = int(input("Enter your security flags (as an integer): "))

if verified == True:           
    if user_id & 1 == 0:       
        if flags & 0b111 != 0: 
            print("✅ Access granted")
        else:
            print("❌ Access denied")
    else:
        print("❌ Access denied")
else:
    print("❌ Access denied")

    
