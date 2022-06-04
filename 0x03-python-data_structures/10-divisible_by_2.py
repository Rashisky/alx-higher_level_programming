#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = [1 if x % 2 == 0 else 0 for x in my_list]
    return new_list
