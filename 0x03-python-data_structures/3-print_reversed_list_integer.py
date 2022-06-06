#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list.copy()
    new_list.reverse()
    [print("{:d}".format(i)) for i in new_list]
