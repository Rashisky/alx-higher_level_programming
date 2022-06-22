#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
