#!/usr/bin/env python3
""" Converts csv to json format"""

import csv
import json
import sys

def csv_to_file(csv_file):
    "Convert csv to file object"
    file_data = open(csv_file, "r", 1, newline='')
    return file_data

def file_to_json(csv_file):
    "Convert file to json"
    csv_reader = csv.DictReader(csv_file)
    csv_info_arr = []
    for row in csv_reader:
        csv_info_arr.append(row)
    json_data = json.dumps(csv_info_arr)
    return json_data

for args in sys.argv[1:]:
    print(file_to_json(csv_to_file(args)))
