#!/usr/bin/python3
for x in range(1, 99):
    if x > 9:
        for i in range(x):
            if f"{i:02d}" == str(x % 10) + str(x // 10):
                x = i
        if (x-1 == i):
            print(f"{x:02d}", end=" ")
    elif x <= 9:
        print(f"{x:02d}", end=" ")
print("\n")
