#!/usr/bin/env python3
""" This script transfers the files listed after the first entry into the selected directory. """

import os
import sys
import string
import shutil

def copy_files(transferFile):
    "copies files to the selected directory mentioned in the transfer file."
    textList = read_file_lines(transferFile)
    for index in range(0, len(textList)):
        textList[index] = textList[index].rstrip("\n")
    transferPath = textList[0]
    fileList = textList[1:] 
    for file in fileList:
        shutil.copy2("./" + file, transferPath)


def read_file_lines(fileName):
    "Reads file input and outputs contents."
    fle = open(fileName, "r", 1)
    contents = fle.readlines()
    fle.close()
    return contents

copy_files(sys.argv[1]) 