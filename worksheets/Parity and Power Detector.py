"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""
# my code
print ("parity and power detector".upper())
number = int(input("Enter number: "))
if number & 1 == 0:
     print("{} is even".format(number))
else:    
     print("{} is odd".format(number))

if  number > 0 and (number & (number - 1)) == 0:
     print("{} is power of 2".format(number))

else:
     print("{} is not power of 2".format(number)) 
