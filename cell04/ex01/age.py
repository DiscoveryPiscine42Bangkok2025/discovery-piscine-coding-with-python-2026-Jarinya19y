#!/usr/bin/env python3
age = int(input("Tell me your age : "))

print("You are currently", age, "years old.")
for i in range (1, 4):
    print("In", i*10, "you will be", (i*10)+age, "years old.")