# your code here
def main():
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ["~", "`", "!", "@", "#", "$" , "%", "^", "&", "*", "(", ")", "_", "-", "'", "<", ">", "?"]
    print(""" 
---Password must at least have:
    1 Number
    1 Symbol
    8 Characters
    """)
    inputs("Name: ")
    # i didn't get what you meant by "if not same as name" so i'm not gonna be doing anything with the name
    
    password = inputs("Password: ")
    p = list(password)
    num = ""
    sym = ""
    valid = True
    if len(p) < 8:
        valid = False
        print("**8 Characters")
    for pa in p:
        if pa in nums: num += pa
        elif pa in symbols: sym += pa
    if not num: 
        valid = False
        print("**1 Number")
    if not sym:
        valid = False
        print("**1 symbol")
    if valid: print("Valid Password!!")
    else: print("Invalid/weak password!!")


def inputs(question):
    while True:
        ans = input(question)
        if ans: return ans
        else: print("Field can't be left empty!! ")



main()