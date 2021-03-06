#!/usr/bin/env python3

import sys
import argparse

def recover(baseChars, twords, ignore=None, delimiter=" "):
    """
    baseChars <-> twords => recovered twords 
    """
    if type(baseChars) == str:
        baseChars = baseChars.split(delimiter) 

    if type(twords) == str:
        twords = twords.split(delimiter)
    
    if type(ignore) == str :
        tline = "".join(twords)
        if tline.startswith(ignore):
            return tline 

    result = []
    tcur = twords.pop(0)
    bcur = baseChars.pop(0)
    while len(bcur) > 0:
        while len(baseChars) > 0 and bcur + baseChars[0] in tcur:
            bcur += baseChars.pop(0)

        index = tcur.find(bcur)
        while index < 0:
            tcur += twords.pop(0) 
            index = tcur.find(bcur)

        result.append(tcur[0:len(bcur)])
        tcur = tcur[len(bcur):]
        bcur = ""
        if len(tcur) == 0 and len(twords) > 0:
            tcur = twords.pop(0)

        if len(baseChars) > 0:
            bcur = baseChars.pop(0)

    return " ".join(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recover half width words segmentation of file2 in file1')
    parser.add_argument('base', type=str,  help='filename of base chars')
    parser.add_argument('target', type=str,  help='filename of segmentation')
    parser.add_argument('--ignore', type=str, default=None, help='line starting from this string is ignored and output the same content')
    args = parser.parse_args()
    
    with open(args.base, "r") as base, open(args.target, "r") as target:
        while True:
            baseLine = base.readline().strip()
            targetLine = target.readline().strip()
            if baseLine == "" or targetLine == "":
                 break

            baseChars = baseLine.split(" ") 
            line = targetLine.split(" ")
            print(recover(baseChars, line, args.ignore))
