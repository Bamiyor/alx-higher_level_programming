#!/usr/bin/python3
for x in range(0, 10):
    for y in range(1, 10):
        if x >= y:
            continue
        else:
            print("{}{},".format(x,y), end=", ")
