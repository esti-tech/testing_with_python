def has_access(verified, user_id, flags):
    return verified and (user_id & 1 == 0) and (flags & 0b111 != 0)


verified = True
user_id = 42
flags = 4  

if has_access(verified, user_id, flags):
    print("✅ Access Granted!")
else:
    print("❌ Access Denied.")
