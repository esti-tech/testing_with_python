# Bitwise Shift Visualizer.py

print("Let’s play with bitwise shifting")

n = int(input("Enter any positive number: "))
print("\nYour number is", n, "which is", bin(n), "in binary.")

i = 1
while i <= 4:
    left = n << i
    right = n >> i
    print("\nShift by", i, "bit(s):")
    print("Left shift:", left, "—", bin(left))
    print("Right shift:", right, "—", bin(right))
    i += 1

print("\nCool, right? That’s how bits move left and right!")
