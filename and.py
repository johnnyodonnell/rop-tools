#!/usr/bin/env python3

import sys


arg1 = sys.argv[1]
arg2 = sys.argv[2]

arg1 = int(arg1, 16)
arg2 = int(arg2, 16)

print(hex(arg1 & arg2))

