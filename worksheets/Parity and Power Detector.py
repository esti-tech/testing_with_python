num = int(input("enter a number:\n"))
if num & 1 == 0:
  print(f"the number {num} is an even number")
else: print(f"the number {num} is an odd number")
if num != 0:
  if (num & (num - 1)) == 0:
    print(f"the number {num} is power of two")
  else: print(f"the number {num} is not power of two")
else: print("0 is not power of two.")

