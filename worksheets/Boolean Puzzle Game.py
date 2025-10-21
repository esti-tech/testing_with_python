"""
You're designing a gate access system. Access is granted only if:

The user is verified (verified == True)
The user has an even ID (id & 1 == 0)
The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""

verified = input("Is user verified? (true/false): ").lower() == "true"
user_id = int(input("Enter user ID: "))
flags = int(input("Enter security flags: "))

access_granted = verified and (user_id & 1 == 0) and (flags & 0b111 != 0)

print(f"\nAccess Granted: {access_granted}")
if access_granted:
    print("Welcome! Access approved.")
else:
    print("Access denied. Check requirements.")
