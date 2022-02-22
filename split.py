import re
import sys
import os

header_pattern = re.compile(":: (.+?)(?: (\[.*\]))?(?: ({.*}))?\n")
# filter_pattern = re.compile("[^a-zA-Z0-9]")
filter_pattern = re.compile("[<>:\"/\\|?*]")

os.mkdir("split")

with open(sys.argv[1], "rt", encoding="utf8") as file:
    for line in file:
        match = header_pattern.match(line)
        if match:
            out = open(f"split/{filter_pattern.sub('_', match[1])}.twee", "wt", encoding="utf8")
        out.write(line)
