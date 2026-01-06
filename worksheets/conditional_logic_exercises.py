print("Conditional Logic Exercises")

#to check if a number is positive or negative or zero
num=float(input("Enter a number: "))
if num>0:
    print("the number that you entered is positive")
elif num <0:
    print("the number that you entered is negative")
else:
    print("the number that you entered is zero")

 # to check if a number is even or odd
num=int(input("Enter a number: "))
if num % 2 == 0:
    print("the number that you entered is even")
else:
    print("the number that you entered is odd")

#to check a number is divisible by 3 and 5
num=input("Enter a number: ")
if int(num) % 3 ==0 and int(num) % 5 ==0:
    print("the number that you entered is divisible by 3 and 5")
else:
    print("the number that you entered is not divisible by 3 and 5")

