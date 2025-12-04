#  petros firist phython converter
print("choose conversion type you want")
print("1. miles to kilometers")
print("2. kilometers to miles")

choice=int(input())
match choice:
   
    case 1:
        mile=float(input("enter the value in miles: "))
        kmeter=mile/0.62
        print(f"{mile} miles = {kmeter} kilometers")
    case 2:
        kmeter=float(input("enter the value in kilometer: "))
        mile=kmeter * 0.62
        print(f"{kmeter} kilometer = {mile} miles")

    case _:
        print("error unapprpriate data")