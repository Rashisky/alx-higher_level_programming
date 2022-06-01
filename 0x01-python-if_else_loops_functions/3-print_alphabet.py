#!/usr/bin/python3
x = 97
while x <= 122:
    if chr(x) == 'e' or char(x) == "q":
        continue
    else:
        print(f"{chr(x)}", end="")
    x += 1
