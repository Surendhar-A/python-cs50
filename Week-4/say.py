# packages - third party libraries
# pypi.org - website to download python packages

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello " + sys.argv[1])
    cowsay.trex("hello " + sys.argv[1])