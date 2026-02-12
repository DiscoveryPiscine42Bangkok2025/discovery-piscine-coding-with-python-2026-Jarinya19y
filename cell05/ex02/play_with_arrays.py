#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22,-12, 2]
print("Original", array)
new = []
for i in array:
    if i > 5 :
        new.add(i+2)
print("New", new)