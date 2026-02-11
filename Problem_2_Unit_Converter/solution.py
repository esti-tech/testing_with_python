# your code here
# my code here
conversion_type = input("which conversion do you want to convert temprature or length? ")
value = float(input("please input value? "))
unit = input("please input unit? ")
if conversion_type=="length":
  if unit == "mi":
     print(value*1.60934,"km")
  else:
      print(value*0.62,"mi")
else:
    if unit == "C":
      print((value*9/5)+32,"Fahrenheit")
    else:
      print((value-32)*5/9,"Celsius")
