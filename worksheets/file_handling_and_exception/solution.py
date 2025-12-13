
def read_announcement():
    with  open(r"C:\Users\user\Desktop\mee\testing_with_python\worksheets\file_handling_and_exception\announcement.txt") as file:
        print(file.read())

read_announcement()

def read_announcement():
    filename = input("enter your file name")
    try:
        with open(filename,"r") as file:
            
            print(file.read())
    except FileNotFoundError:
        print("the file name  you entered was not found") 
read_announcement()           

def read_file():
     with open(r"C:\Users\user\Desktop\mee\testing_with_python\worksheets\file_handling_and_exception\students.csv") as file:
         print(file.read())
read_file()       


