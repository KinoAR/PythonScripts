#!/usr/bin/env python3
""" This program writes a text file with a specified name. """

import sys #import the sys module in Python

print(sys.argv) # print sys.argv or system arguments to output
NAME = sys.argv[1] #Represents second argument passed to program
FILENAME = open(NAME, "w+", 1)
# Open the file for writing and create it doesn't exist
