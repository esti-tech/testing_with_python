verified=True
user_id=1024
flags=0b1010
if not verified:
     print("Access denied:user not verified")
elif user_id&1!=0:
     print("Access define: user id is not even")
elif flags & 0b111==0:
     print("Access denied:security flags don't meet requirements")
else:
     print("Access granted!")
