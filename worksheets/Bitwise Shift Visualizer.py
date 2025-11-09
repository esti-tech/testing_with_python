integer_1=int(input("Enter first number: "))
shift=int(input("Enter number of shif positions: "))
print("original number: "+integer_1)
print ("binary( befor shift):"+ bin(integer_1))


left_shift = integer_1<<shift
print("After left shift "+shift +" positions :")
print("Decimal :"+left_shift+".")
print("binary: "+bin(left_shift))

right_shift=integer_1 >> shift
print("after right shift "+shift +"positions: ")
print("decimal: "+right_shift) 
print("binary: "+bin(right_shift))
