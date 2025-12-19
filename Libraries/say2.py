#documentation : https://docs.python.org/3/library/sys.html
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    print("Hello,", sys.argv[1])