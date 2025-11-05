
verified = input("Is user verified? (yes/no): ").lower() == "yes"
user_id = int(input("Enter user ID: "))
flags = int(input("Enter security flags (as an integer): "))

if verified:
    if user_id % 2 == 0:
        if flags & 0b111 != 0:
            print("Access granted.")
        else:
            print("Access denied: No security flag in last 3 bits.")
    else:
        print("Access denied: User ID is not even.")
else:
    print("Access denied: User not verified.")

