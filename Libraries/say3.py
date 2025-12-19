#documentation : https://docs.python.org/3/library/sys.html
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("Hello, mam na imie", arg)