print("Conditional Logic Exercises")
# Practice if/elif/else statements here.
num = int(input("Input an integer: "))
if num & 1 == 0:
    print("even")
else:
    print("odd")
if num > 0 and (num & (num - 1)) == 0:
    print("is a power of two")
else:
    print("is not a power of two")
