verified = input("Is the user verified? (yes/no): ").strip().lower() == "yes"
user_id = int(input("Enter user ID (integer): "))
flags = int(input("Enter security flags (as integer): "))
is_even_id = (user_id & 1) == 0
has_flag_in_last_3_bits = (flags & 0b111) != 0
access_granted = verified and is_even_id and has_flag_in_last_3_bits
print("\nAccess Check:")
print(f"Verified: {verified}")
print(f"User ID Even: {is_even_id}")
print(f"Flags (last 3 bits not all zero): {has_flag_in_last_3_bits}")
print("\nAccess Granted:" if access_granted else "\nAccess Denied.")
