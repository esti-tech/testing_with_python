import string

password = input("Enter password: ")

length_ok = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_special = any(c in string.punctuation for c in password)

print("Length >= 8:", length_ok)
print("Has uppercase:", has_upper)
print("Has lowercase:", has_lower)
print("Has special char:", has_special)
