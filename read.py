#!/usr/bin/env python3
"""This program reads a file given a specific input and outputs it to standard output"""
FILENAME = input("Enter the filename: ")
def readfile(filename):
    "Reads file input and outputs contents."
    fle = open(filename, "r", 1)
    print(fle.read())
    fle.close()

readfile(FILENAME)
