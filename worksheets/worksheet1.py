# accept shift value from the user
num = int(input("Enter any integer: "))
shift = int(input("How many positions to shift? "))

#set original number and in binary form
print("Number:", num)
print("Binary:", bin(num))

# Left shift
left_shift = num << shift
print(f"{num} << {shift} = {left_shift}")
print("Binary:", bin(left_shift))

# Right shift
right_shift = num >> shift
print(f"{num} >> {shift} = {right_shift}")
print("Binary:", bin(right_shift))
