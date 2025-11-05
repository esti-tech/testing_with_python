# print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.
# my code
print("welcom to data type conversion!")
number = input("please enter the number: ")
try:
 print("as_intiger = {}". format(int(number)))
 print("as_boolean = {}". format(bool(number)))
 print("as_string = {}". format(str(number)))
 print("as_float = {}". format(float(number)))
except ValueError:
 print("error:{} can't be converted". format(number))
