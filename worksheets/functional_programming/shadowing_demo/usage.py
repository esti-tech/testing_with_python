# usage.py

# TODO: Write code that fails when using local list.py
# TODO: Fix by importing builtins and using builtins.list explicitly

# Example starter:
# try:
#     a = list((1,2,3))
#     print(a)
# except TypeError:
#     import builtins
#     print(builtins.list((1,2,3)))
# usage.py

try:
    a = list((1, 2, 3))
    print(a)

except TypeError:
    print("TypeError occurred because local list.py shadowed the built-in 'list'.")
    import builtins
    a = builtins.list((1, 2, 3))
    print("Fixed version:", a)

