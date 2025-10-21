"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""
# boolean_puzzle_game.py

def is_verified():
    response = input("Is the user verified? (yes/no): ").strip().lower()
    return response == "yes"

def get_user_id():
    return int(input("Enter the user ID (integer): "))

def get_security_flags():
    return int(input("Enter the security flags (0–255): "))

def check_access(verified, user_id, flags):
    even_id = (user_id & 1) == 0
    has_flag_bit = (flags & 0b111) != 0

    print("\n--- Access Check ---")
    print(f"Verified?          : {verified}")
    print(f"User ID            : {user_id} ({'Even' if even_id else 'Odd'})")
    print(f"Flags (binary)     : {bin(flags)}")
    print(f"Last 3 bits        : {bin(flags & 0b111)}")

    # Access logic
    if verified and even_id and has_flag_bit:
        return True
    return False

# Run the puzzle game
print("=== Boolean Puzzle Game: Gate Access ===")

verified = is_verified()
user_id = get_user_id()
flags = get_security_flags()

if check_access(verified, user_id, flags):
    print("\n✅ Access Granted!")
else:
    print("\n❌ Access Denied.")