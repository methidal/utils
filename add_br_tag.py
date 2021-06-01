#accept input file containing poem without br tag
#go through one line at a time
#to each line add <br> tag
#print line with <br> tag added

import sys

input_file = sys.argv[1]

for line in file(input_file):
    line = line.strip()
    line = line + ' <br> '
    print line