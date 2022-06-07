#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = -1
    for i in my_list:
        print("{:d}".format(my_list[x]))
        x -= 1
