#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        element = my_list[i]
        try:
            print("{:d}".format(element), end="")
            count += 1
        except Exception as e:
            pass
        i += 1
    print('\n')
    return count
