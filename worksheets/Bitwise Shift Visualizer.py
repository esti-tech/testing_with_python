"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
#my code
number = int(input("enter a number? "))
shift_position= int(input("enter number of shift? "))

print ("left shift << {}".format(shift_position))
left_shift = number << shift_position
print (left_shift)
print ("right shift >> {}".format(shift_position))
right_shift = number >> shift_position
print (right_shift)

print ("BEFORE AND AFTER LEFT SHIFT")
print ("binary number before left shift = {}" .format (bin(number)))
print ("binary number after  left shift = {}" .format (bin(left_shift)))


print ("BEFORE AND AFTER RIGHT SHIFT")
print ("binary number before right shift = {}" .format (bin(number)))
print ("binary number after  right shift = {}" .format (bin(right_shift)))
