#!/usr/bin/env python3

import fileinput
import re
import sys
import argparse

import utils

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

def annotate(tags, tokens, baseChars):
    if type(tags) == str:
        tags = tags.split(" ")

    if type(tokens) == str:
        tokens = tokens.split(" ")

    if type(baseChars) == str:
        baseChars = baseChars.split(" ")

    if tags[0].startswith("rejected") or tokens[0].startswith("rejected"):
        return "rejected"
        
    buffer = []
    cur = 0
    for wordIndex, token in enumerate(tokens):
        sourceCategory = ""
        eIndices = {} 
        while token != "": 
            assert token.startswith(baseChars[cur])
            newCategory = getCategory(tags[cur])
            if sourceCategory == "":
                sourceCategory = newCategory
            elif sourceCategory != newCategory:
                return "ignored"

            matchObj = re.search(r"\((.*)\)", tags[cur])
            assert matchObj is not None, "eIndices are not specified in %s" % (args.tagfile,)
            eIndicesString = matchObj.groups()[0]
            if eIndicesString != "":
                for index, tag in map(lambda x: x.split(":"), eIndicesString.split(",")):
                    if sourceCategory == "possible":
                        eIndices[index] = "possible"
                    else:
                        eIndices[index] = "sure" if tag == "" else "possible"

            token = token[len(baseChars[cur]):]
            cur += 1
        else:
            for eIndex in eIndices:
                buffer.append("%d-%s[%s]" % (wordIndex, eIndex, eIndices[eIndex]))

    return " ".join(buffer)

def getCategory(linkTag):
    if linkTag.startswith("NTR") or linkTag.startswith("MTA") or linkTag.startswith("TIN"):
        return "ntr"
    elif ":TRA" in linkTag:
        return "sure"
    else:
        return "possible"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
""")
    parser.add_argument('tagfile', type=str, help='tagfile')
    parser.add_argument('tokenfile', type=str, help='tokenfile')
    parser.add_argument('base', type=str, help='filename for base characters')
    args = parser.parse_args()

    with open(args.tagfile, "r") as tagfile, open(args.tokenfile, "r") as tokenfile, open(args.base, "r") as base:
        while True:
            tagLine = tagfile.readline().strip()
            tokenLine = tokenfile.readline().strip()
            baseLine = base.readline().strip()
            if tagLine == "" or tokenLine == "" or baseLine == "":
                break

            tags = tagLine.split(" ")
            tokens = tokenLine.split(" ")
            baseChars = baseLine.split(" ")

            print(annotate(tags, tokens, baseChars)) 
