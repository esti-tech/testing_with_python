print("simple unit converter")
print("choose conversion type you want")
print("1. kilometers to miles")
print("2. miles to kilometers")


choice=int(input())
match choice:
    case 1:
        kmeter=float(input("enter the value in kilometer: "))
        mile=kmeter * 0.62
        mile=round(mile,2)
        print(f"{kmeter} kilometer = {mile} miles")

    case 2:
        mile=float(input("enter the value in miles: "))
        kmeter=mile/0.62
        kmeter=round(kmeter,2)
        print(f"{mile} miles = {kmeter} kilometers")

    case _:
        print("invalid choice please select the correct option")