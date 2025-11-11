def check_access(verified, user_id, flags):
    if not verified:
        return "Access denied: User not verified."
    if user_id & 1 != 0:
        return "Access denied: User ID is not even."
    if flags & 0b111 == 0:
        return "Access denied: Security flag does not contain a 1 in the last 3 bits."
    
    return "Access granted.
verified = input("Is the user verified? (True/False): ").strip().lower() == 'true'
user_id = int(input("Enter the user's ID: "))
flags = int(input("Enter the security flag (as an integer): "))
result = check_access(verified, user_id, flags)
print(result)
