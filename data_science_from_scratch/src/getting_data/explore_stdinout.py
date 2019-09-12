# egrep.py

# standard libraries
import sys

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line

print(f"Length of Sys.argv is: {len(sys.argv)}" )

for index, args in enumerate(sys.argv):
    print(f"Sys.argv[{index}] is: {sys.argv[index]}" )
    print(f"Type of Sys.argv[{index}] is: {type(sys.argv)}" )

# for index, args in enumerate(sys.stdin):
    print(f"Sys.argv[{index}] is: {sys.argv[index]}" )
    print(f"Type of Sys.argv[{index}] is: {type(sys.argv)}" )