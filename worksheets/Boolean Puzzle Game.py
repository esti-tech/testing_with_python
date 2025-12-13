"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""
def check_gate_access():
    """
    Checks if a user is granted access based on the three security criteria.
    Access is granted only if ALL three conditions are True.
    """
    print("--- Gate Access System Check ---")

    # 1. Get user inputs
    try:
        verified_input = input("Is the user verified? (True/False): ").strip().lower()
        verified = verified_input == 'true'
        
        user_id = int(input("Enter user ID (integer): "))
        
        # Read security flags as a decimal integer
        security_flags = int(input("Enter security flags (integer value): "))
        
    except ValueError:
        return "Error: Please enter valid inputs (True/False for verification, integers for ID and Flags)."

    # 2. Check the three required conditions
    
    # Condition A: The user is verified (verified == True)
    condition_a = verified
    
    # Condition B: The user has an even ID (id & 1 == 0)
    # Checks if the last bit is 0 (even) using Bitwise AND.
    condition_b = (user_id & 1) == 0
    
    # Condition C: The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
    # 0b111 is the mask to check the last three bits.
    condition_c = (security_flags & 0b111) != 0

    # 3. Access is granted only if ALL three conditions are TRUE.
    access_granted = condition_a and condition_b and condition_c

    # 4. Print the result
    print("\n--- CHECK RESULTS ---")
    print(f"Condition A (Verified): {condition_a}")
    print(f"Condition B (Even ID): {condition_b}")
    print(f"Condition C (Flags Check): {condition_c}")
    
    if access_granted:
        return "ACCESS GRANTED."
    else:
        return "ACCESS DENIED. One or more conditions failed."

# Run the function and print the final output
if __name__ == "__main__":
    print(check_gate_access())