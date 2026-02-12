#!/usr/bin/env python3
first_num = int(input("Input the first number : "))
second_num = int(input("Input the second number : "))
mul = first_num * second_num

print(first_num, "x", second_num, "=", mul)

if (mul == 0):
    print("This number is both positive and negative.")
elif (mul >= 0):
    print("This number is positive.")
else :
    print("This number is negative.")