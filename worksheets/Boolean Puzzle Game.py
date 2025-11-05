verified = bool(int(input("Is user verified? (1 for Yes, 0 for No): ")))
user_id = int(input("Enter user ID: "))
security_flag = int(input("Enter security flag (integer): "))


if verified and ((user_id & 1) == 0) and (security_flag & 0b111 != 0):
    print(" Access Granted")
else:
    print(" Access Denied")