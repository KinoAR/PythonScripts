#!/usr/bin/env python3
""" Create a project skeleton"""

import zipfile
import urllib.request
import sys
import os

def download_file(address):
    "Download file from the internet"
    downloaded_file = urllib.request.urlopen(address)
    data = downloaded_file.read()
    zip_file = open("tmp.zip", "wb+", 1)
    zip_file.write(data)
    zip_file.close()
    return zip_file

def unzip(zip_file, directory_name):
    "Unzip file, extract to folder, and remove temporary zip file"
    if zipfile.is_zipfile(zip_file):
        zip_ref = zipfile.ZipFile(zip_file, "r")
        zip_ref.extractall()
        print("Extracted project-skeleton to {0}".format(directory_name))
        os.rename("project-skeleton-master", directory_name)
        os.remove(zip_file)

ARGS = sys.argv
DOWNLOAD = download_file("https://github.com/KinoAR/project-skeleton/archive/master.zip")
unzip(DOWNLOAD.name, ARGS[1:2][0])
