import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
"""
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

name = sys.argv[1]
print("Hello, My name is", name)
"""

for i in sys.argv[1:]:
    print("Hello, My name is", i)
