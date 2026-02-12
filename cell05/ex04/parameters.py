#!/usr/bin/env python3
import sys
print("Numbers of parameters : ", end="")
if len(sys.argv) == 1:
    print(0)
else: 
    print(len(sys.argv) - 1)