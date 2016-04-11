#!/usr/bin/env python3

import fileinput
import re
import sys
import argparse
import mojimoji

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

def containHankaku(s):
    return mojimoji.zen_to_han(s) == s and mojimoji.han_to_zen(s) != s:

def isAscii(c):
    return ord(c) < 128

def getCategory(linkTag):
    if ":TRA" in linkTag:
        return "sure"
    elif linkTag.startswith("NTR") or linkTag.startswith("MTA"):
        return "ntr"
    else:
        return "possible"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
""")
    parser.add_argument('tagfile', type=str, help='tagfile')
    parser.add_argument('tokenfile', type=str, help='tokenfile')
    args = parser.parse_args()

    tokenNum = 0
    sentenceNum = 0
    multipleTagTokenNum = 0
    multipleTagSentenceNum = 0
    with open(args.tagfile, "r") as tagfile, open(args.tokenfile, "r") as tokenfile:
        while True:
            tagline = tagfile.readline().rstrip()
            tags = re.split(r" +", tagline)
            tokenline = tokenfile.readline().rstrip()
            tokens = re.split(r" +", tokenline)
            tokenNum += len(tokens)
            buffer = []
            if tagline=="" or tokenline=="":
                break

            cur = 0
            for wordIndex, token in enumerate(tokens):
                category = ""
                eIndices = set()

                for i in range(len(token)):
                    # if isSymbol(token[i]) and i < len(token) - 1 and isSymbol(token[i+1]):
                    if containHankaku(token[i]) and i < len(token) - 1 and containHankaku(token[i+1]):
                        continue

                    newCategory = getCategory(tags[cur])
                    # print(newCategory)
                    if category == "":
                        category = newCategory
                    elif category != newCategory:
                        buffer = None
                        break

                    matchObj = re.search(r"\((.*)\)", tags[cur])
                    assert matchObj is not None, "eIndices are not specified in %s" % (args.tagfile,)
                    eIndicesString = matchObj.groups()[0]
                    if eIndicesString != "":
                        eIndices.update(eIndicesString.split(","))

                    cur += 1
                else:
                    for eIndex in eIndices:
                        buffer.append("%d-%s[%s]" % (wordIndex,eIndex,category))

                if buffer is None:
                    break

            if buffer is None: 
                print("ignored")
            else:
                print(" ".join(buffer))
