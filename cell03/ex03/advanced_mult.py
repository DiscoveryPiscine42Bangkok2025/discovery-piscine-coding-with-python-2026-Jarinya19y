#!/usr/bin/env python3
import sys

if len(sys.argv) > 1: 
    print("none")
else:
    i = 0
    while (i < 11):
        print("Table de", i, ": ", end="")
        n = 0
        while (n < 11) :
            print(i * n, end=" ")
            n+=1
        print()
        i+=1