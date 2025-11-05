"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""


verified = input("Is the user verified? (yes/no): ").lower() == "yes"
user_id = int(input("Enter user ID (integer): "))
flags = int(input("Enter security flags (integer): "))

if verified:
    if (user_id & 1) == 0:  
        if (flags & 0b111) != 0:  
            print("✅ Access granted.")
        else:
            print("❌ Access denied: No active security bits in last 3 positions.")
    else:
        print("❌ Access denied: User ID must be even.")
else:
    print("❌ Access denied: User not verified.")
