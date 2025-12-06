#Input an integer.
#Print:
#Whether it’s even or odd using num & 1
#Whether it’s a power of two using (num & (num - 1)) == 0
num = int(input("Enter a number: "))
print(f"{num} is {'even' if num % 2 == 0 else 'odd'}")
if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a power of 2")
else:
    print(f"{num} is not a power of 2")
