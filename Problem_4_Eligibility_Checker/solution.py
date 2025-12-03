# your code here
def main():
    while True:
        age = to_num("Age: ")
        license = inputs("License status(good, bad): ")
        if age >= 18 and license.lower() in ["good", "g"]:
            print("Eligible")
            out()
        else:
            print("Not Eligible")
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