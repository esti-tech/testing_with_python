"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)
eee
The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""

print("gate access system")
verified_input = input("Are you verified? (Yes/No): ")
if verified_input == "Yes":
    verified_input= True
else:
    verified_input= False
user_id = int(input("Enter user_id: "))
flags = int(input("Enter security flags: "))
if verified_input and (user_id & 1 == 0) and (flags & 0b111 != 0):
    print("access granted")
else:
    print("access denied")