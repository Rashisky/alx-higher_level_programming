#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = {}
    for k, v in sorted(a_dictionary.items()):
        result = f"{k}: {v}"
        a.update({k: v})
        print(result)
    return a
