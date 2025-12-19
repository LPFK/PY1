from saying0 import Hello, Goodbye
import sys
if len(sys.argv) == 2:
    Hello(sys.argv[1])
    Goodbye(sys.argv[1])
    