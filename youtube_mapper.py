# Author: Dongqi Xu (480529282)
#!/usr/bin/python3

import sys


def tag_mapper():
    first_line = True
    for line in sys.stdin:
        if first_line:
            first_line = False
        else:
            parts = line.strip().split(",")
            print("{}\t{}\t{}".format(parts[3], parts[0], parts[-1]))

if __name__ == "__main__":
    tag_mapper()
