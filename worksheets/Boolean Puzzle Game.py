def check_access(user_id, verified, flags):

    if not verified:
        return "Access Denied: User not verified."

    if user_id & 1 != 0:
        return "Access Denied: User ID is not even."

    if flags & 0b111 == 0:
        return "Access Denied: Security flags do not meet criteria."

    return "✅ Access Granted"
