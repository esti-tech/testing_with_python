a = input("Enter any character to check the type: ")

print(f"Original type of a: {type(a)}")

try:
    print(f"int of a = {int(a)}")
except x:
    print(f"Cannot convert '{a}' to int")

try:
    print(f"float of a = {float(a)}")
except x:
    print(f"Cannot convert '{a}' to float")

print(f"string of a = {str(a)}")
print(f"complex of a = {complex(a)}")
