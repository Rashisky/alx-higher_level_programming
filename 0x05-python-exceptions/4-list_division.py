#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            try:
                new_list.append(x / y)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except Exception as e:
                print("wrong type")
                new_list.append(0)
        except Exception as e:
           print("out of range")
           new_list.append(0)
        i += 1
    return new_list
