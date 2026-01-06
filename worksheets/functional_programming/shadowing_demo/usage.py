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
#
try:
    a = list((1, 2, 3))  
    print(a)
except Exception as e:
    print("Error:", e)
    print("Local list.py shadowed the built-in list!")

    # Fix: use the real built-in list explicitly
    import builtins
    correct_list = builtins.list((1, 2, 3))
    print("Correct list using builtins:", correct_list)



