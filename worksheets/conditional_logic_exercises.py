#("Conditional Logic Exercises")
# Practice if/elif/else statements here.
# Parity and Power Detector
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")
