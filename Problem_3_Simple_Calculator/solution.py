#Problem 3:Simple calculater

print("===simple calculator===")
print("1.Addition(+)")
print("2.Substraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

choice = input("choose operation (1/2/3/4):")

if choice in ["1","2","3","4"]:
  num1 = float(input("Enter the first number:"))
  num2 = float(input("Enter the second number:"))     

  if choice =="1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

  elif choice =="2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

  elif choice =="3":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

  elif choice =="4":
    if num2!=0:
      result = num1 / num2
      print(f"{num1} / {num2} = {result}")

    else:
      print("Error:cannot divide by zero!")
      result = "undefined"
      
      #Add the final result line (only if we have a valid result)
      if choice!="4" or (choice =="4" and num2!=0):
        print("Result:", result)

      else:
        print("Invalid Choice!Please Enter 1,2,3,4.")
      
  
               
               
