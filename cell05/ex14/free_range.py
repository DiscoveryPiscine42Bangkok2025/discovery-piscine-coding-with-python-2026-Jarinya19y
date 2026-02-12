#!/usr/bin/env python3
import sys
if len(sys.argv) != 3:
    print("none")
else:
    sys.argv.pop(0)
    arr = 0
    n = range(int(sys.argv[0]), int(sys.argv[1]))
    for i in n:
        arr.append(i)
    print(arr)