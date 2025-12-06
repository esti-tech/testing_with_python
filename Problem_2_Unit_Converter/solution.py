#1. Ask which conversion user wants.
print("choose a conversion:")
print("1.kilometer to meter:")
print("2.meter to kilometer:")
print("3.celsius to fahrenit:")
print("4.fahrenit to celsius:")
#take choice input
choice =int(input("enter your choice (1-4):"))
#2. Input value.
value=float (input("enter the value to convert:"))
#3. Convert and print result.
if choice==1:
  result =value*1000
  print(f"{value:.2f}km ={result:.2f} m")
elif choice==2:
  result=value/1000
  print(f"{value:.2f}m={result:.2f} km")
elif choice==3:
  result=(value*9/5)+32
  print(f"{value:.2f}c={result:.2f}f")
elif choice ==4:
  result=(value-32)*5/9
  print (f"{value:.2f}f={result:.2f}c")
else:
  print ("invalid option!please choose anumber betweeen 1 and 4")
