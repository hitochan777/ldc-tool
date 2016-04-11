#!/usr/bin/env python3

import fileinput
import re
import sys

"""
SEM Semantic link
FUN Function link
PDE DE-possessive link
CDE DE-clause link
MDE DE-modifier link
GIF Grammatically Inferred Function link
GIS Grammatically Inferred Semantic link
COI Contextually Inferred link
TIN (Translated) Incorrect link
NTR Not Translated link
MTA link for Meta word
"""

def isSymbol(c):
    symbols = ["。", "？", "！", "…"]
    return ord(c) < 128 or c.isdigit() or c.isalpha() or c in symbols

def getCategory(linkTag):
    if linkTag.endswith(":TRA"):
        return "S"
    elif linkTag.startswith("NTR") or linkTag.startswith("MTA"):
        return "NTR"
    else:
        return "P"

if __name__ == "__main__":
    tokenNum = 0
    sentenceNum = 0
    multipleTagTokenNum = 0
    multipleTagSentenceNum = 0
    with open(sys.argv[1], "r") as tagfile, open(sys.argv[2], "r") as tokenfile:
        while True:
            tagline = tagfile.readline().rstrip()
            tags = re.split(r" +", tagline)
            tokenline = tokenfile.readline().rstrip()
            tokens = re.split(r" +", tokenline)
            tokenNum += len(tokens)
            if tagline=="" or tokenline=="":
                break
            hasMultiple = False            
            cur = 0
            for token in tokens:
                s = set()
                for i in range(len(token)):
                    if isSymbol(token[i])  and i < len(token) - 1 and isSymbol(token[i+1]):
                        continue
                    category = getCategory(tags[cur])

                    s.add(category)
                    if len(s) > 1:
                        multipleTagTokenNum += 1
                        hasMultiple = True
                        break

                    cur += 1

            if hasMultiple:
                multipleTagSentenceNum += 1
            sentenceNum += 1


        print("# of token with multiple tags = %d" % multipleTagTokenNum)
        print("total token = %d" % tokenNum)
        print("# of sentence with multiple tags = %d" % multipleTagSentenceNum)
        print("total sentence = %d" % sentenceNum)
