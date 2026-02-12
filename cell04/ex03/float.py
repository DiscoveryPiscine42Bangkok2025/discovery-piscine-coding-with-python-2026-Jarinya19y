#!/usr/bin/env python3
num = float(input("Gimme number : "))
if ((num * 10) % 10) == 0 :
    print("This number is integer.")
else:
    print("This number is decimal.")