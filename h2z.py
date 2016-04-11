#!/usr/bin/env python3

import fileinput

import mojimoji

for line in fileinput.input():
    print(mojimoji.han_to_zen(line), end="")
