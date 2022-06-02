#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 0:
        print(f"{length} arguments.")
    else:
        print(f"{length} arguments:")
        for i in range(1, length + 1):
            print(f"{i}: {sys.argv[i]}")
