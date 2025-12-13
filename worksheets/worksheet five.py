#accept input from users

num = int(input("Enter an integer: "))

# Check  even or odd 
if num & 1 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")
