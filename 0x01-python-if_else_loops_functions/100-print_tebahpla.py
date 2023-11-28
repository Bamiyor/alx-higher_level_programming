#!/usr/bin/python3
i = 0
for x in range(ord('z'), ord('a')-1, -1):
    print("{}".format(chr(x-i) if i == 32 else i-32), end="")
