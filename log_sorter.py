#!/usr/bin/env python
from datetime import datetime
import re
import getopt, sys

# CONSTANTS
verboseMode = 0
versionNumber = "1.2a"
updatedOn = "11/11/2017"

inFileName = "file.txt"
outFileName = "outfile.txt"
sorted_outlog = []

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

def get_args():
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

def sort_log_by_time(in_log, arg='desc'):
   test_file = open(in_log,"r")
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
   return trinary_list

def write_file(out_log, out_file, args='append'):

   wf = open(out_file,"a")

   for i in out_log:
       wf.write(i[1] + "\n\n")


get_args()
sorted_outlog = sort_log_by_time(inFileName)

write_file(sorted_outlog, outFileName)
