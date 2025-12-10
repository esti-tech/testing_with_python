"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""

#Gate Access System
print("===Gate Access Control===")

#Get user input
verified =input("Is user verified? (true/false):").lower()=="true"
user_id =int(input("Enter user ID:"))
flag =int(input("Enter security flags (as integer):"))

#Check access conditions
condition1 =verified==True
condition2 =(user_id&1)==0 #Even ID check
condition3 =(flags&0b111)!=0 #Last 3 bits check

#Determine access
access_granted =condition1 and condition2 and condition3

print(f"\n---Access Check Results---")
print(f"1.User verified:{condition1}")
print(f"2.Even ID{user_id}):{condition2}")
print(f"3.Security flags valid ({bin(flags)}):{condition3}")

if access_granted:
  print("ACCESS GRANTED-All conditions met!")
else:
  print("ACCESS DENIED-Missing condition:")
  if not condition1:
    print(" -user not verified")
  if not condition2:
    print(" -ID is not even")
  if not condition3:
    print(" -security flags invalid (last 3 bits are 000)")
    
    
               
