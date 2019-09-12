# most_common_words.py

# standard libraries
import sys
from collections import Counter

# pass in number of words as first argument
try: 
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py num_words")
    sys.exit(1)     # nonzero exit code indicates an error

counter = Counter(word.lower()          # lowercase words
                    for line in sys.stdin
                    for word in line.strip().split()
                    if word
    )