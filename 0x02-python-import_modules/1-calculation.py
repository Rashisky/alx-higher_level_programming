#!/usr/bin/python3
import calculator_1 as cal
if __name__ == "__main__":
    a = 10
    b = 5
    c = cal.add(a, b)
    d = cal.sub(a, b)
    e = cal.mul(a, b)
    f = cal.div(a, b)
    print(f"{a} {+} {b} = {c}")
    print(f"{a} {-} {b} = {d}")
    print(f"{a} {*} {b} = {e}")
    print(f"{a} {/} {b} = {f}")
