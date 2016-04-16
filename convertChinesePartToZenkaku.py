#!/usr/bin/env python3

import sys
import argparse

import mojimoj

"""
"""

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()
    with open(args.input,"r") as i:
        for line in i:
            line = line.strip()
            if line.startswith("zh:"):
                result = []
                tokens = line.split(" ")
                for token in tokens:
                    result.append(mojimoji.han_to_zen(token))

                print("zh: %s" % (" ".join(result)))

            else:
                print(line)
