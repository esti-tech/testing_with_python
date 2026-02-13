#problem 5
def simple_passwared_check(passward):
    has_upper = any(c.isupper() for c in passward)
    has_lower = any(c.islower() for c in passward)
    has_digit = any(c.isdigit() for c in passward)
    has_special = any(not c.isalnum() for c in passward)
    if len(passward) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "strong"
    elif len(passward) >= 6 and (has_upper or has_lower) and has_digit:
        return "medium"
    else:
        return "weak"
