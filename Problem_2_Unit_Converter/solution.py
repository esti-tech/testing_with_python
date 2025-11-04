#Problem 2:Unit Converter 

print("===unit converter===")
print("1.miles to kilometers")
print("2.celsius to fahrenheit")
choice =input("choose conversion (1 or 2):")

if choice =="1":
#miles to kilometers 
miles = float(input("Enter distance in miles:"))
kilometers = miles*1.60934
print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")

elif choice =="2":
#Celsius to Fahrenheit 
celsius = float(input("Enter temperature in celsius:"))
fahrenheit = (celsius*9/5)+32
print(f"{celsius} deg c is equal to{fahrenheit:.2f} deg f.")

else:
print("Invalid choice! Please Enter 1 or 2.")