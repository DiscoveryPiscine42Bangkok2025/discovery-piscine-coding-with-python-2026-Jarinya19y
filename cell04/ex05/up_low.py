#!/usr/bin/env python3
txt = input()

for i in txt :
    if i.islower():
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")
print()