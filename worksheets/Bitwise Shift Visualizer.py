"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""

#Bit shifting with explanations
num =int(input("Enter integer:"))
shift =int(input("Shift positions:"))
print(f"\noriginal:{num} = {bin(num)}")

#Left shift:moves bits left,multiplies by 2
left_result =num<<shift
print(f"Left <<{shift}:{left_result}={bin(left_result)}")
print(f"Each Left shift multiplies by 2:{num}*2^{shift}={num*(2**shift)}")

#Right shift:moves bits right,divides by 2
right_result=num>>shift
print(f"Right>>{shift}:{right_result}={bin(right_result)}")
print(f"Each Right shift divides by 2:{num}//2^{shift}={num//(2**shift)}")
