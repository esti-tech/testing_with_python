"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""
def check_gate_access(verified, user_id, flags):

    return verified and (user_id & 1 == 0) and (flags & 0b111 != 0)
print(check_gate_access(True, 10, 5))
print(check_gate_access(True, 7, 5))
print(check_gate_access(False, 10, 5))
print(check_gate_access(True, 10, 8))
