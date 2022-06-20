#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for element in my_list:
        try:
            print(element, end="")
            count += 1
        except Exception as e:
            break
    print("")
    return (count)