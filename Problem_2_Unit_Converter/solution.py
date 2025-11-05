# your code here
def main():
    while True:
        print("1. Convert miles to kilometers")
        print("2. Celsius to Fahrenheit.") 
        print("3. Exit")
        choice = to_num(": ")
        if choice == 1:
            mile = to_num("Mile: ", "f")
            print(f"Mile => Km = {mile * 1.60934} ")
            out()
        elif choice == 2:
            cel = to_num("Celsius: ", "f")
            print(f"Cel => Fah = {(cel * 9/5) + 32} ")
            out()
        elif choice == 3: exit(0)
        else: 
            input("Invalid!!!! ")
            out()

def inputs(question):
    while True:
        ans = input(question)
        if ans: return ans
        else: print("Field can't be left empty!! ")

def to_num(question, f="i"):
    while True:
        i = inputs(question)
        try:
            if f == "f": i_i = float(i)
            else: i_i = int(i)
        except Exception: 
            print("Only input a number!!")
        else:
            return i_i
def out():
    while True:
        ans = inputs("Do you want to go again?(y/n) ").upper()
        if ans == "Y" or ans == "YES": break 
        elif ans == "N" or ans == "NO": exit(0) 


main()
           