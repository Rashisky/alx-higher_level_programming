#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 0:
        print(f"{length}")
    else:
        result = 0
        for i in range(1, length + 1):
            i = int(sys.argv[i])
            result = result + i
        print(f"{result}")
