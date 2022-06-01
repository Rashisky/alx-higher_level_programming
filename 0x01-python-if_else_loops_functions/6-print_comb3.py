#!/usr/bin/python3
for x in range(1, 99):
    if x > 9 and x != 89:
        for i in range(x):
            if f"{i:02d}" == str(x % 10) + str(x // 10):
                i = 0
        if (x-1 == i):
            print("{:02d}".format(x), end=" ")
    elif x <= 9:
        print("{:02d}".format(x), end=" ")
    else:
        print("{:02d}".format(x))
