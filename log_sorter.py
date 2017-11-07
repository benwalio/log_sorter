#!/usr/bin/env python
from datetime import datetime
import re
import getopt, sys

# CONSTANTS
verboseMode = 0
versionNumber = "1.0a"
updatedOn = "11/02/2017"

inFileName = "file.txt"
outFileName = "outfile.txt"
# fullCmdArgs = sys.argv
# argList = fullCmdArgs[1:]


def set_outfile(file_name):
   global outFileName
   outFileName = file_name
   print (("output file is - %s") % (outFileName))

def set_infile(file_name):
   global inFileName
   inFileName = file_name
   print (("input file is - %s") % (inFileName))

def set_verbose_mode(toggle):
   if toggle == 1:
      verboseMode = 1
   elif toggle == 0:
      verboseMode = 0
   else:
      print "unable to set verbose mode to " + str(toggle) + "\nExiting..."
      quit_program()

def quit_program():
   sys.exit()

class get_args():
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
       quit_program()

# loads arguments
   for currentArgument, currentValue in arguments:
       if currentArgument in ("-h"):
           print ("slack Ben if you need help for now\nSTOPPING...")
           quit_program()
       elif currentArgument in ("-v"):
           set_verbose_mode(1)
       elif currentArgument in ("-o"):
           set_outfile(currentValue)
       elif currentArgument in ("-a"):
           print (("version number is - %s") % (versionNumber))
       elif currentArgument in ("-i"):
           set_infile(currentValue)

class sort_log():
   global inFileName
   global outFileName

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


get_args()
sort_log()

# test_file = open(inFileName,"r")
# read_file = test_file.read()
#
# read_file2 = read_file.split("\n\n")
# trinary_list = []
#
# datetime_format = re.compile("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
#
# for i in range(len(read_file2)):
#     current_line = read_file2[i]
#     match2 = re.search(datetime_format, current_line)
#     if match2:
#         hold_tups = (match2.group(),read_file2[i])
#         trinary_list.append(hold_tups)
#
# trinary_list.sort()
#
# wf = open(outFileName,"a")
#
# for i in trinary_list:
#     wf.write(i[1] + "\n\n")
