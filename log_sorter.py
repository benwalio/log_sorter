#!/usr/bin/env python
from datetime import datetime
import re
import getopt, sys

# CONSTANTS
verboseMode = 0
versionNumber = "1.0a"
updatedOn = "11/02/2017"

# defaults to
inFileName = "file.txt"
outFileName = "outfile.txt"

fullCmdArgs = sys.argv
argList = fullCmdArgs[1:]


# define arguments
#   a- version number
#   o- ouput file, requires variable
#   i- input file, requires variable
#   v- version number
macArgs = "aho:i:v"

try:
    arguments, values = getopt.getopt(argList, macArgs)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit()

# loads arguments
for currentArgument, currentValue in arguments:
    if currentArgument in ("-h"):
        print ("slack Ben if you need help for now\n STOPPING")
        sys.exit()
    elif currentArgument in ("-v"):
        verboseMode = 1
        print ("enabling verbose mode - jokes on you, this is the only verbosity you get - don't get greedy")
    elif currentArgument in ("-o"):
        outFileName = currentValue
        print (("output set to - %s") % (currentValue))
    elif currentArgument in ("-a"):
        print (("version number is - %s") % (versionNumber))
    elif currentArgument in ("-i"):
        inFileName = currentValue
        print (("input file is - %s") % (inFileName))


test_file = open(inFileName,"r")
read_file = test_file.read()

read_file2 = read_file.split("\n\n")
trinary_list = []

datetime_format = re.compile("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

for i in range(len(read_file2)):
    current_line = read_file2[i]
    match2 = re.search(datetime_format, current_line)
    if match2:
        hold_tups = (match2.group(),read_file2[i])
        trinary_list.append(hold_tups)

trinary_list.sort()

wf = open(outFileName,"a")

for i in trinary_list:
    wf.write(i[1] + "\n\n")
