
num = int(input("Enter a number: "))
shift = int(input("Enter how many bits to shift: "))

left_shift = num << shift
right_shift = num >> shift

print("Original number:", num)
print("After left shift:", left_shift)
print("After right shift:", right_shift)
