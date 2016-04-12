#!/usr/bin/env python3

import sys
import argparse
from bisect import *
from itertools import accumulate
from collections import defaultdict

import utils

def recover(sline, tline):
    """
    sline <-> tline => recovered tline
    漢 漢 10 漢 <-> 漢 漢10漢 => 漢 漢 10 漢
    漢 漢 10 漢 <-> 漢漢 1 0漢 => 漢漢 10 漢
    漢 漢 10 20 漢 <-> 漢 漢1 020漢 => 漢 漢 10 20 漢
    """
    swords = sline.split(" ")
    twords = tline.split(" ")
    swords = list(filter(lambda word: not utils.containChineseCharacter(word), swords))
    result = []
    tcur = twords.pop(0)
    while len(swords) > 0:
        if utils.isChineseString(tcur):
            result.append(tcur)
            if len(twords) > 0:
                tcur = twords.pop(0)
        else:
            index = tcur.find(swords[0])
            while index < 0: 
                tcur += twords.pop(0) 
                index = tcur.find(swords[0])
            
            if index > 0:
                result.append(tcur[:index])
                tcur = tcur[index:]
            
            result.append(tcur[:len(swords[0])])
            tcur = tcur[len(swords[0]):]
            if len(tcur) == 0 and len(twords) > 0:
                tcur = twords.pop(0)

            swords.pop(0)
    
    if tcur != "":
        result += [tcur]

    result += twords
    return " ".join(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recover half width words segmentation of file2 in file1')
    parser.add_argument('source', type=str,  help='source file')
    parser.add_argument('target', type=str,  help='target file')
    args = parser.parse_args()
    
    with open(args.source, "r") as source, open(args.target, "r") as target:
        while True:
            sline = source.readline().strip()
            tline = target.readline().strip()
            if sline=="" or tline=="":
                 break

            print(recover(sline, tline))   
