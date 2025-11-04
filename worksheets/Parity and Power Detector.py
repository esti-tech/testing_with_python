"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""

#Bitwise operation checker
#Get user input
num =int(input("Enter an integer:"))

#Check if even or odd using num & 1
if num & 1:
  print(f"{num} is Odd")
else:
  print(f"{num} is Even")

#Check if power of two using (num & (num-1))==0
if num>0 and (num & (num-1))==0:
  print(f"{num} is a Power of Two")
else:
  print(f"{num} is Not a power of two")
  
