while True:
    print("\n--- Simple Calculator----")
    print("Type 'quit' anytime to exit.")


x = input("Enter The First Number : ")
s_x = int(x)
if s_x.lower()=='quit':
    break

sign = input("Enter The Operation (+, -, *, /) : ")
if sign.lower()=='quit':
    break

y = input("Enter The Second Number : ")
s_y = int(y)
if s_y.lower()=='quit':
    break
  
if sign == "+":
    print("The Sum Is : ", s_x + s_y)
elif sign == "-":
	print("The Difference Is : ", s_x - s_y)
elif sign == "*":
	print("The Product Is : ", s_x * s_y)
elif sign == "/":
	if s_y != 0:
		print("The Quotient Is : ", s_x / s_y)
	else:
		print("Error: Division by zero is not allowed.")


else:
	print("Invalid Operation")

