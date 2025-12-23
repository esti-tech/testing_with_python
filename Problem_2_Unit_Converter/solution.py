# 1. Ask the conversion of user wants ,let 1 Mile =1/0.621371 KM 
print("Choose conversion type:")
print("1. Miles to Kilometers")
print("2. Kilometers to Miles")
Choice = input('Enter 1 or 2 : ')
if Choice == "1":
    miles = float(input("Enter distance in miles: "))
    kilometers = miles / 0.621371 #kilometers = miles * 1.60934
    print(f"{miles} miles = {kilometers:.3f} kilometers")

elif Choice == "2":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371 
    print(f"{kilometers} kilometers = {miles:.3f} miles")
else:
    print('Invalid choice.')
