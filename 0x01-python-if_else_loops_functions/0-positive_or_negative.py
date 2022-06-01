#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is positive")
    break
elif number == 0:
    print(number, "is zero")
    break
else:
    print(number, "is negative")
    break
