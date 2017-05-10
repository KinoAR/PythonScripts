#!/usr/bin/env python3
""" This script gives you the area of a particular shape using the information you enter."""
import re
import math

SHAPEINPUT = input("Enter shape of choice: ")

def area(shape,):
    "Calculates the area of any particular shape"
    param1 = 0
    param2 = 0
    param3 = 0

    if re.search(r"square", shape, re.I):
        param1 = float(input("Enter Length: "))
        param2 = float(input("Enter Width: "))
        print("The area is: " + str(param1 * param2))
    elif re.search(r"circle", shape, re.I):
        param1 = float(input("Enter Radius: "))
        print("The area is: " + str(math.pi * param1 ** 2))
    elif re.search(r"triangle", shape, re.I):
        param1 = float(input("Enter Base: "))
        param2 = float(input("Enter Height: "))
        print("The area is: " + str(param1 * param2 / 2))
    elif re.search(r"trapezoid", shape, re.I):
        param1 = float(input("Enter Base1: "))
        param2 = float(input("Enter Base2: "))
        param3 = float(input("Enter Height: "))
        print("The area is: " + str((param1 + param2)/ 2 * param3))
    else:
        print("You entered an invalid shape.")

area(SHAPEINPUT)
