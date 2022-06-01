#!/usr/bin/python3
for x in range(1, 100):
    if x > 9:
        for i in range(x):
            c = str(x % 10) + str(x // 10)
            if f"{i:02d}" == c:
                break
        if (x-1 == i):
            print(f"{x:02d}", end=" ")
    elif x <= 9:
        print(f"{x:02d}", end=" ")
    x += 1
print("\n")
