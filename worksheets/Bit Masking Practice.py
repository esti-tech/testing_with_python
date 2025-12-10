READ    = 0b001  
WRITE   = 0b010  
EXECUTE = 0b100  

user_perm = READ | EXECUTE
print(f"Current permissions: {bin(user_perm)}")  

if user_perm & WRITE:
    print("User can write")
else:
    print("User cannot write")

user_perm = user_perm | WRITE
print(f"After adding WRITE: {bin(user_perm)}")  

user_perm = user_perm & ~EXECUTE
print(f"After removing EXECUTE: {bin(user_perm)}")  

user_perm = user_perm ^ READ
print(f"After toggling READ: {bin(user_perm)}")  
