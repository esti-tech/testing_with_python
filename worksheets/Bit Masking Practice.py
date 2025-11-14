num = int(input("Enter a number: "))
mask = int(input("Enter a bit mask: "))
and_result = num & mask
or_result = num | mask
xor_result = num ^ mask
print(f"{num} & {mask} = {and_result}")
print(f"{num} | {mask} = {or_result}")
print(f"{num} ^ {mask} = {xor_result}")
