#!/usr/bin/env python3

import sys
import fileinput
import re
import argparse

"""
    this script extracts words and word alignment simultaneously from the file where the format follows the files in this directory whose extension is 'wa'
"""

def process(buffer):
    if len(buffer)!=3:
        sys.exit("len(buffer) is not 3")
    if "rejected" in buffer[2]:
        return []
    fchars = buffer[0].rstrip().split()[1:] # remove the first word "zh:"
    return "".join(fchars)

if __name__=="__main__":
    parser = argparse.ArgumentParser(prog="./extract.py")
    parser.add_argument("input", help="input file")
    args = parser.parse_args()
    with open(args.input,"r") as i:
        buffer = []
        for line in i:
            if line.startswith("#") and len(buffer)==3:
                print(process(buffer))
                buffer = []
            elif not line.startswith("#"):
                buffer.append(line)

        if len(buffer)==3:
            print(process(buffer))
