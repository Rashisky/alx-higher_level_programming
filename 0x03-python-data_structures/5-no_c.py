#!/usr/bin/python3
def no_c(my_string):
    my_list = [x for x in my_string if (x != "c" and x != 'C')]
    new_string = "".join(my_list)
    return (new_string)
