#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for values in matrix:
        for elements in values:
            if elements != values[-1]:
                print("{:d}".format(elements), end=" ")
            else:
                print("{:d}".format(elements))
