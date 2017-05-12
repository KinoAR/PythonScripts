#!/usr/bin/env python3
""" This script creates the meteor folder structure given a starting directory """

import os
import sys

def create_meteor_struct(startpath):
    "creates the meteor directory"
    pathlist = ["/imports/startup/client", "/imports/startup/server", "/ui/components",
                "/client/stylesheets", "/server", "/public/images", "/node_modules"]
    for path in pathlist:
        os.makedirs(startpath+path, exist_ok=True)
    return

create_meteor_struct(sys.argv[1])
