print("this code is for checking eligibility for drivind license")
print("please enter your age! ")
age = int(input())
while True:
    license = input("do u have a license? (yes/no): )").lower()
    if license in ["yes", "no"]:
        break
    else:
        print("please enter 'yes' or 'no'!")
if age >= 18:
    if license == "yes":
        print("you are a legit person to drive")
    else:
        print("you are old enough to have a license but u need a license to drive! ")
else:
    print("you are not a legit person to drive")