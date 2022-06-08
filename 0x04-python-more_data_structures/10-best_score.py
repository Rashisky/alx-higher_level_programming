#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    Max = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v == Max:
            return k
