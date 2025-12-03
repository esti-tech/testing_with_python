"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""

# i used chatGPT for the idea here because i didn't know what you wanted us to do here 
# but i only used GPT for the array idea part. 


def can_access(verified, user_id, flags):
    return verified and ((user_id & 1) == 0) and ((flags & 0b111) != 0)

users = [
    {"verified": True, "id": 10, "flags": 0b010}, 
    {"verified": False, "id": 10, "flags": 0b010},
    {"verified": True, "id": 11, "flags": 0b010},
    {"verified": True, "id": 10, "flags": 0b000},
]

for u in users:
    status = "granted" if can_access(u['verified'], u['id'], u['flags']) else "denied"
    print(f"User {u['id']}: Access {status}")
