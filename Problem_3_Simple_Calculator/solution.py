# your code here
# my code
print("welcome to mini calculator!")
print("what kind of operation do you want to operate?")
print("For addition 1,for subtraction 2, for multiplication 3, for division 4 and for module 5")

operation_type=input("inter the number to proceed operation ")
if operation_type not in ["1", "2", "3", "4", "5"]:
    print("Invalid operation selected!")
else:
 value_1 = float(input("input the first number "))
 value_2 = float(input("input the second number ")) 

 if operation_type=="1":
    sum=value_1 + value_2
    print("the sum is",sum)

 elif  operation_type=="2":
    subtract=value_1 - value_2
    print("the subtract is",subtract)

 elif  operation_type=="3":
    multiply=value_1 * value_2
    print("the multiply is",multiply)

 elif  operation_type=="4":
    if value_2 ==0:
        print("mathematical error")
    else:    
     divide=value_1 / value_2
     print("the divide is",divide)
   
 elif operation_type == "5":
    if value_2 == 0:
        print("mathematical error: modulo by zero")
    else:
        module = value_1 % value_2
        print("the module is", module)
