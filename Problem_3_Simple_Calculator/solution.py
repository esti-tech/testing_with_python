# your code here
def main():
    while True:
        num_1 = to_num("First Number: ", "f")
        num_2 = to_num("Second Number: ", "f")
        while True:
            oper = inputs("Operator: ")
            if oper in ["+", "-", "*", "/", "//", "**"]:
                equ = str(num_1) + oper + str(num_2)
                try:
                    answer = eval(equ)
                except Exception as e:
                    print(f"Error: {e}")
                    break
                else: 
                    print(f"Answer: {answer}")
                    out()
                    break
            else: 
                print("Unknown operator!!")
                out()
                break
            

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